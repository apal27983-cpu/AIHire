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

from app.schemas.application import (
    ApplicationResponse,
    UpdateApplicationStatus
)

from app.services.application_service import (
    apply_for_job,
    get_my_job_applications,
    get_applications_for_job,
    update_application_status
)

router = APIRouter(
    prefix="/applications",
    tags=["Applications"]
)


@router.post(
    "/{job_id}",
    response_model=ApplicationResponse
)
def apply_job(
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

        return apply_for_job(
            db,
            current_user.id,
            job_id
        )

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get(
    "/my",
    response_model=List[ApplicationResponse]
)
def my_applications(
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):
    return get_my_job_applications(
        db,
        current_user.id
    )


@router.get(
    "/job/{job_id}",
    response_model=List[ApplicationResponse]
)
def job_applications(
    job_id: int,
    db: Session = Depends(get_db)
):
    return get_applications_for_job(
        db,
        job_id
    )


@router.put(
    "/{application_id}/status",
    response_model=ApplicationResponse
)
def change_status(
    application_id: int,
    request: UpdateApplicationStatus,
    db: Session = Depends(get_db)
):
    try:
        return update_application_status(
            db,
            application_id,
            request.status
        )

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )