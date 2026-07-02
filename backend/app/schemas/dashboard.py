from pydantic import BaseModel


class RecruiterDashboardResponse(
    BaseModel
):
    total_jobs: int
    total_applications: int
    shortlisted_candidates: int
    scheduled_interviews: int

class CandidateDashboardResponse(
    BaseModel
):
    applied_jobs: int
    shortlisted_jobs: int
    upcoming_interviews: int


#Admin Dashboard
class AdminDashboardResponse(
    BaseModel
):
    total_users: int
    total_candidates: int
    total_recruiters: int
    total_companies: int
    total_jobs: int
    total_applications: int
    total_interviews: int