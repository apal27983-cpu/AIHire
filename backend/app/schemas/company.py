from pydantic import BaseModel


class CompanyCreate(BaseModel):
    name: str
    website: str | None = None
    industry: str | None = None
    location: str | None = None


class CompanyResponse(CompanyCreate):
    id: int

    class Config:
        from_attributes = True