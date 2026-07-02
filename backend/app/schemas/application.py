from pydantic import BaseModel
from datetime import datetime


class ApplicationResponse(BaseModel):
    id: int
    candidate_id: int
    job_id: int
    status: str
    application_source: str
    applied_at: datetime

    class Config:
        from_attributes = True


class UpdateApplicationStatus(BaseModel):
    status: str