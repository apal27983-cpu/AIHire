from sqlalchemy.orm import Session

from app.models.job import Job
from app.repositories.job_repository import (
    create_job,
    get_all_jobs,
    get_job_by_id,
    get_jobs_by_recruiter
)
from app.repositories.recruiter_repository import (
    get_recruiter_by_user_id
)


def create_new_job(
    db: Session,
    user_id: int,
    data
):
    recruiter = get_recruiter_by_user_id(
        db,
        user_id
    )

    if not recruiter:
        raise Exception(
            "Recruiter profile not found"
        )

    job = Job(
        company_id=recruiter.company_id,
        recruiter_id=recruiter.id,
        title=data.title,
        description=data.description,
        skills_required=data.skills_required,
        experience_required=data.experience_required,
        salary_min=data.salary_min,
        salary_max=data.salary_max,
        location=data.location,
        job_type=data.job_type
    )

    return create_job(
        db,
        job
    )


def get_jobs(
    db: Session
):
    return get_all_jobs(db)


def get_job(
    db: Session,
    job_id: int
):
    job = get_job_by_id(
        db,
        job_id
    )

    if not job:
        raise Exception(
            "Job not found"
        )

    return job


def get_my_jobs(
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

    return get_jobs_by_recruiter(
        db,
        recruiter.id
    )