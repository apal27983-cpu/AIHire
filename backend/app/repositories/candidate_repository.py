from sqlalchemy.orm import Session
from app.models.candidate import Candidate


def get_candidate_by_user_id(
    db: Session,
    user_id: int
):
    return (
        db.query(Candidate)
        .filter(Candidate.user_id == user_id)
        .first()
    )


def create_candidate(
    db: Session,
    candidate: Candidate
):
    db.add(candidate)
    db.commit()
    db.refresh(candidate)
    return candidate