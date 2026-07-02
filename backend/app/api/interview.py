from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)
from sqlalchemy.orm import Session
from typing import List

from app.db.database import get_db
from app.schemas.interview import (
    InterviewCreate,
    InterviewUpdate,
    InterviewResponse
)
from app.services.interview_service import (
    schedule_interview,
    get_interviews,
    update_interview_status
)
from app.api.dependencies import get_current_user
from app.models.user import User

router = APIRouter(
    prefix="/interviews",
    tags=["Interviews"]
)


@router.post(
    "/",
    response_model=InterviewResponse
)
def create_interview(
    request: InterviewCreate,
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

        return schedule_interview(
            db,
            request.application_id,
            request.scheduled_at,
            request.meeting_link
        )

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get(
    "/",
    response_model=List[InterviewResponse]
)
def get_all_interviews(
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):
    return get_interviews(db)


@router.put(
    "/{interview_id}",
    response_model=InterviewResponse
)
def update_interview(
    interview_id: int,
    request: InterviewUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):
    try:
        return update_interview_status(
            db,
            interview_id,
            request.status,
            request.feedback
        )

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )