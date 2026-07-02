from sqlalchemy.orm import Session
from app.models.interview import Interview


def create_interview(
    db: Session,
    interview: Interview
):
    db.add(interview)
    db.commit()
    db.refresh(interview)
    return interview


def get_interview_by_id(
    db: Session,
    interview_id: int
):
    return (
        db.query(Interview)
        .filter(Interview.id == interview_id)
        .first()
    )


def get_all_interviews(
    db: Session
):
    return db.query(Interview).all()


def save(db: Session):
    db.commit()