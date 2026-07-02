from sqlalchemy.orm import Session
from app.models.recruiter import Recruiter


def get_recruiter_by_user_id(
    db: Session,
    user_id: int
):
    return (
        db.query(Recruiter)
        .filter(Recruiter.user_id == user_id)
        .first()
    )


def create_recruiter(
    db: Session,
    recruiter: Recruiter
):
    db.add(recruiter)
    db.commit()
    db.refresh(recruiter)
    return recruiter