from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Text,
    DateTime
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base import Base


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)

    company_id = Column(
        Integer,
        ForeignKey("companies.id"),
        nullable=False
    )

    recruiter_id = Column(
        Integer,
        ForeignKey("recruiters.id"),
        nullable=False
    )

    title = Column(String, nullable=False)
    description = Column(Text)
    skills_required = Column(Text)
    experience_required = Column(Integer)
    salary_min = Column(Integer)
    salary_max = Column(Integer)
    location = Column(String)
    job_type = Column(String)
    status = Column(String, default="OPEN")

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    company = relationship(
        "Company",
        back_populates="jobs"
    )

    recruiter = relationship(
        "Recruiter",
        back_populates="jobs"
    )

    applications = relationship(
        "Application",
        back_populates="job"
    )