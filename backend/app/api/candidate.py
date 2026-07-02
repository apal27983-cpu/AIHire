from fastapi import UploadFile, File
import os
import shutil
from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.candidate import (
    CandidateCreate,
    CandidateResponse
)
from app.api.dependencies import get_current_user
from app.models.user import User
from app.services.candidate_service import (
    create_candidate_profile,
    get_my_candidate_profile
)
from app.services.resume_parser import (
    extract_text_from_pdf,
    extract_skills
)

router = APIRouter(
    prefix="/candidate",
    tags=["Candidate"]
)
UPLOAD_DIR = "uploads/resumes"

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)


@router.post(
    "/profile",
    response_model=CandidateResponse
)
def create_profile(
    request: CandidateCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):
    try:
        if current_user.role != "candidate":
            raise HTTPException(
                status_code=403,
                detail="Only candidates allowed"
            )

        return create_candidate_profile(
            db,
            current_user.id,
            request.phone,
            request.experience,
            request.current_location,
            request.preferred_location,
            request.skills,
            request.resume_url
        )

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get(
    "/profile",
    response_model=CandidateResponse
)
def get_profile(
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):
    try:
        return get_my_candidate_profile(
            db,
            current_user.id
        )

    except Exception as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )
    

@router.post("/upload-resume")
def upload_resume(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):
    try:
        if current_user.role != "candidate":
            raise HTTPException(
                status_code=403,
                detail="Only candidates allowed"
            )

        if not file.filename.endswith(".pdf"):
            raise HTTPException(
                status_code=400,
                detail="Only PDF files allowed"
            )

        filename = (
            f"user_{current_user.id}.pdf"
        )

        file_path = os.path.join(
            UPLOAD_DIR,
            filename
        )

        with open(
            file_path,
            "wb"
        ) as buffer:
            shutil.copyfileobj(
                file.file,
                buffer
            )

        profile = get_my_candidate_profile(
            db,
            current_user.id
        )

        profile.resume_url = file_path
        db.commit()
        db.refresh(profile)

        return {
            "message": "Resume uploaded successfully",
            "resume_url": file_path
        }

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

@router.post("/parse-resume")
def parse_resume(
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):
    try:
        profile = get_my_candidate_profile(
            db,
            current_user.id
        )

        if not profile.resume_url:
            raise HTTPException(
                status_code=400,
                detail="Resume not uploaded"
            )

        text = extract_text_from_pdf(
            profile.resume_url
        )

        skills = extract_skills(
            text
        )

        profile.skills = ", ".join(
            skills
        )

        db.commit()
        db.refresh(profile)

        return {
            "skills": skills,
            "resume_text_preview":
                text[:1000]
        }

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )