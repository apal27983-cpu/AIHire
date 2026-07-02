from sqlalchemy.orm import Session
from app.models.application import Application


def create_application(
    db: Session,
    application: Application
):
    db.add(application)
    db.commit()
    db.refresh(application)
    return application


def get_application(
    db: Session,
    candidate_id: int,
    job_id: int
):
    return (
        db.query(Application)
        .filter(
            Application.candidate_id == candidate_id,
            Application.job_id == job_id
        )
        .first()
    )


def get_my_applications(
    db: Session,
    candidate_id: int
):
    return (
        db.query(Application)
        .filter(
            Application.candidate_id == candidate_id
        )
        .all()
    )


def get_job_applications(
    db: Session,
    job_id: int
):
    return (
        db.query(Application)
        .filter(
            Application.job_id == job_id
        )
        .all()
    )


def get_application_by_id(
    db: Session,
    application_id: int
):
    return (
        db.query(Application)
        .filter(
            Application.id == application_id
        )
        .first()
    )


def save(db: Session):
    db.commit()