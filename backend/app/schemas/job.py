from pydantic import BaseModel


class JobCreate(BaseModel):
    title: str
    description: str
    skills_required: str
    experience_required: int
    salary_min: int
    salary_max: int
    location: str
    job_type: str


class JobResponse(JobCreate):
    id: int
    company_id: int
    recruiter_id: int
    status: str

    class Config:
        from_attributes = True