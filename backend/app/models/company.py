from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base import Base


class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    website = Column(String)
    industry = Column(String)
    location = Column(String)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    recruiters = relationship(
        "Recruiter",
        back_populates="company"
    )

    jobs = relationship(
        "Job",
        back_populates="company"
    )