from sqlalchemy.orm import Session
from app.models.interview import Interview
from app.repositories.interview_repository import (
    create_interview,
    get_interview_by_id,
    get_all_interviews,
    save
)


def schedule_interview(
    db: Session,
    application_id: int,
    scheduled_at,
    meeting_link: str
):
    interview = Interview(
        application_id=application_id,
        scheduled_at=scheduled_at,
        meeting_link=meeting_link
    )

    return create_interview(
        db,
        interview
    )


def get_interviews(
    db: Session
):
    return get_all_interviews(db)


def update_interview_status(
    db: Session,
    interview_id: int,
    status: str,
    feedback: str = None
):
    interview = get_interview_by_id(
        db,
        interview_id
    )

    if not interview:
        raise Exception(
            "Interview not found"
        )

    interview.status = status
    interview.feedback = feedback

    save(db)

    return interview