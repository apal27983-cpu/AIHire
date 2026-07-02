from sqlalchemy.orm import Session

from app.models.candidate import Candidate
from app.repositories.candidate_repository import (
    get_candidate_by_user_id,
    create_candidate
)


def create_candidate_profile(
    db: Session,
    user_id: int,
    phone: str,
    experience: int,
    current_location: str,
    preferred_location: str,
    skills: str,
    resume_url: str
):
    existing_candidate = get_candidate_by_user_id(
        db,
        user_id
    )

    if existing_candidate:
        raise Exception(
            "Candidate profile already exists"
        )

    candidate = Candidate(
        user_id=user_id,
        phone=phone,
        experience=experience,
        current_location=current_location,
        preferred_location=preferred_location,
        skills=skills,
        resume_url=resume_url
    )

    return create_candidate(
        db,
        candidate
    )


def get_my_candidate_profile(
    db: Session,
    user_id: int
):
    candidate = get_candidate_by_user_id(
        db,
        user_id
    )

    if not candidate:
        raise Exception(
            "Candidate profile not found"
        )

    return candidate