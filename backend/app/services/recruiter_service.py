from sqlalchemy.orm import Session

from app.models.recruiter import Recruiter
from app.repositories.recruiter_repository import (
    get_recruiter_by_user_id,
    create_recruiter
)


def create_recruiter_profile(
    db: Session,
    user_id: int,
    company_id: int,
    designation: str,
    phone: str
):
    existing = get_recruiter_by_user_id(
        db,
        user_id
    )

    if existing:
        raise Exception(
            "Recruiter profile already exists"
        )

    recruiter = Recruiter(
        user_id=user_id,
        company_id=company_id,
        designation=designation,
        phone=phone
    )

    return create_recruiter(
        db,
        recruiter
    )


def get_my_recruiter_profile(
    db: Session,
    user_id: int
):
    recruiter = get_recruiter_by_user_id(
        db,
        user_id
    )

    if not recruiter:
        raise Exception(
            "Recruiter profile not found"
        )

    return recruiter