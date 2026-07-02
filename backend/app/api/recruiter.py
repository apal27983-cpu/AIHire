from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.api.dependencies import get_current_user
from app.models.user import User
from app.schemas.recruiter import (
    RecruiterCreate,
    RecruiterResponse
)
from app.services.recruiter_service import (
    create_recruiter_profile,
    get_my_recruiter_profile
)

router = APIRouter(
    prefix="/recruiter",
    tags=["Recruiter"]
)


@router.post(
    "/profile",
    response_model=RecruiterResponse
)
def create_profile(
    request: RecruiterCreate,
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

        return create_recruiter_profile(
            db,
            current_user.id,
            request.company_id,
            request.designation,
            request.phone
        )

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get(
    "/profile",
    response_model=RecruiterResponse
)
def get_profile(
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):
    return get_my_recruiter_profile(
        db,
        current_user.id
    )