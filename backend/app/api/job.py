from typing import List

from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.api.dependencies import get_current_user
from app.models.user import User

from app.schemas.job import (
    JobCreate,
    JobResponse
)

from app.services.job_service import (
    create_new_job,
    get_jobs,
    get_job,
    get_my_jobs
)
from app.services.job_matching_service import (
    calculate_match_score
)
from app.services.candidate_service import (
    get_my_candidate_profile
)
from app.services.application_service import (
    get_applications_for_job
)

from app.services.candidate_ranking_service import (
    rank_candidates
)

router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"]
)


@router.post(
    "",
    response_model=JobResponse
)
def create_job(
    request: JobCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):
    try:
        if current_user.role != "recruiter":
            raise HTTPException(
                status_code=403,
                detail="Only recruiters allowed"
            )

        return create_new_job(
            db,
            current_user.id,
            request
        )

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get(
    "",
    response_model=List[JobResponse]
)
def get_all_jobs(
    db: Session = Depends(get_db)
):
    return get_jobs(db)


@router.get(
    "/my-jobs",
    response_model=List[JobResponse]
)
def my_jobs(
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):
    return get_my_jobs(
        db,
        current_user.id
    )


@router.get(
    "/{job_id}",
    response_model=JobResponse
)
def get_single_job(
    job_id: int,
    db: Session = Depends(get_db)
):
    try:
        return get_job(
            db,
            job_id
        )

    except Exception as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )
    

@router.get("/{job_id}/match")
def get_job_match(
    job_id: int,
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

        candidate = get_my_candidate_profile(
            db,
            current_user.id
        )

        job = get_job(
            db,
            job_id
        )

        if not candidate.skills:
            raise HTTPException(
                status_code=400,
                detail="Candidate skills not found. Parse resume first."
            )

        result = calculate_match_score(
            candidate.skills,
            job.skills_required
        )

        return {
            "job_id": job.id,
            "job_title": job.title,
            **result
        }

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
    
@router.get("/{job_id}/rank-candidates")
def get_ranked_candidates(
    job_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):
    try:
        if current_user.role != "recruiter":
            raise HTTPException(
                status_code=403,
                detail="Only recruiters allowed"
            )

        job = get_job(
            db,
            job_id
        )

        applications = get_applications_for_job(
            db,
            job_id
        )

        return rank_candidates(
            applications,
            job
        )

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )