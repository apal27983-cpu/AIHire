from sqlalchemy.orm import Session

from app.models.application import Application
from app.repositories.application_repository import (
    create_application,
    get_application,
    get_my_applications,
    get_job_applications,
    get_application_by_id,
    save
)
from app.repositories.candidate_repository import (
    get_candidate_by_user_id
)
from app.repositories.job_repository import (
    get_job_by_id
)


def apply_for_job(
    db: Session,
    user_id: int,
    job_id: int
):
    candidate = get_candidate_by_user_id(
        db,
        user_id
    )

    if not candidate:
        raise Exception(
            "Candidate profile not found"
        )

    job = get_job_by_id(
        db,
        job_id
    )

    if not job:
        raise Exception(
            "Job not found"
        )

    existing = get_application(
        db,
        candidate.id,
        job_id
    )

    if existing:
        raise Exception(
            "Already applied to this job"
        )

    application = Application(
        candidate_id=candidate.id,
        job_id=job_id
    )

    return create_application(
        db,
        application
    )


def get_my_job_applications(
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

    return get_my_applications(
        db,
        candidate.id
    )


def get_applications_for_job(
    db: Session,
    job_id: int
):
    return get_job_applications(
        db,
        job_id
    )


def update_application_status(
    db: Session,
    application_id: int,
    status: str
):
    application = get_application_by_id(
        db,
        application_id
    )

    if not application:
        raise Exception(
            "Application not found"
        )

    application.status = status
    save(db)

    return application