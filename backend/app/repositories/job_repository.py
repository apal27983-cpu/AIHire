from sqlalchemy.orm import Session
from app.models.job import Job


def create_job(
    db: Session,
    job: Job
):
    db.add(job)
    db.commit()
    db.refresh(job)
    return job


def get_all_jobs(db: Session):
    return db.query(Job).all()


def get_job_by_id(
    db: Session,
    job_id: int
):
    return (
        db.query(Job)
        .filter(Job.id == job_id)
        .first()
    )


def get_jobs_by_recruiter(
    db: Session,
    recruiter_id: int
):
    return (
        db.query(Job)
        .filter(Job.recruiter_id == recruiter_id)
        .all()
    )