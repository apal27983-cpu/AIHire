from pydantic import BaseModel


class CandidateCreate(BaseModel):
    phone: str
    experience: int
    current_location: str
    preferred_location: str
    skills: str
    resume_url: str


class CandidateResponse(CandidateCreate):
    id: int
    user_id: int

    class Config:
        from_attributes = True