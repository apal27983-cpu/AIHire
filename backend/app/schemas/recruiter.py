from pydantic import BaseModel


class RecruiterCreate(BaseModel):
    company_id: int
    designation: str
    phone: str


class RecruiterResponse(RecruiterCreate):
    id: int
    user_id: int

    class Config:
        from_attributes = True