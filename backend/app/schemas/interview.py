from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class InterviewCreate(BaseModel):
    application_id: int
    scheduled_at: datetime
    meeting_link: str


class InterviewUpdate(BaseModel):
    status: str
    feedback: Optional[str] = None


class InterviewResponse(BaseModel):
    id: int
    application_id: int
    scheduled_at: datetime
    meeting_link: str
    status: str
    feedback: Optional[str]

    class Config:
        from_attributes = True