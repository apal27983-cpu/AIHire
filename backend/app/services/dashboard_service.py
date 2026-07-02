from sqlalchemy.orm import Session
from app.models.job import Job
from app.models.application import Application
from app.models.interview import Interview
from app.models.recruiter import Recruiter
from app.models.candidate import Candidate
from app.models.user import User
from app.models.company import Company


def get_recruiter_dashboard(
    db: Session,
    user_id: int
):
    recruiter = (
        db.query(Recruiter)
        .filter(
            Recruiter.user_id == user_id
        )
        .first()
    )

    if not recruiter:
        raise Exception(
            "Recruiter profile not found"
        )

    total_jobs = (
        db.query(Job)
        .filter(
            Job.recruiter_id == recruiter.id
        )
        .count()
    )

    recruiter_jobs = (
        db.query(Job.id)
        .filter(
            Job.recruiter_id == recruiter.id
        )
        .all()
    )

    job_ids = [
        job.id
        for job in recruiter_jobs
    ]

    if not job_ids:
        return {
            "total_jobs": 0,
            "total_applications": 0,
            "shortlisted_candidates": 0,
            "scheduled_interviews": 0
        }

    total_applications = (
        db.query(Application)
        .filter(
            Application.job_id.in_(job_ids)
        )
        .count()
    )

    shortlisted_candidates = (
        db.query(Application)
        .filter(
            Application.job_id.in_(job_ids),
            Application.status == "SHORTLISTED"
        )
        .count()
    )

    scheduled_interviews = (
        db.query(Interview)
        .join(
            Application,
            Interview.application_id
            == Application.id
        )
        .filter(
            Application.job_id.in_(job_ids)
        )
        .count()
    )

    return {
        "total_jobs": total_jobs,
        "total_applications":
            total_applications,
        "shortlisted_candidates":
            shortlisted_candidates,
        "scheduled_interviews":
            scheduled_interviews
    }


#Candidate Dashboard
def get_candidate_dashboard(
    db: Session,
    user_id: int
):
    candidate = (
        db.query(Candidate)
        .filter(
            Candidate.user_id == user_id
        )
        .first()
    )

    if not candidate:
        raise Exception(
            "Candidate profile not found"
        )

    applied_jobs = (
        db.query(Application)
        .filter(
            Application.candidate_id
            == candidate.id
        )
        .count()
    )

    shortlisted_jobs = (
        db.query(Application)
        .filter(
            Application.candidate_id
            == candidate.id,
            Application.status
            == "SHORTLISTED"
        )
        .count()
    )

    upcoming_interviews = (
        db.query(Interview)
        .join(
            Application,
            Interview.application_id
            == Application.id
        )
        .filter(
            Application.candidate_id
            == candidate.id,
            Interview.status
            == "SCHEDULED"
        )
        .count()
    )

    return {
        "applied_jobs":
            applied_jobs,
        "shortlisted_jobs":
            shortlisted_jobs,
        "upcoming_interviews":
            upcoming_interviews
    }


#Admin Dashboard
def get_admin_dashboard(
    db: Session
):
    return {
        "total_users":
            db.query(User).count(),

        "total_candidates":
            db.query(Candidate).count(),

        "total_recruiters":
            db.query(Recruiter).count(),

        "total_companies":
            db.query(Company).count(),

        "total_jobs":
            db.query(Job).count(),

        "total_applications":
            db.query(Application).count(),

        "total_interviews":
            db.query(Interview).count()
    }