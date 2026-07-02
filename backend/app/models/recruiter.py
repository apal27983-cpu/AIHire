from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base


class Recruiter(Base):
    __tablename__ = "recruiters"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    company_id = Column(
        Integer,
        ForeignKey("companies.id"),
        nullable=False
    )

    designation = Column(String)
    phone = Column(String)

    user = relationship(
        "User",
        back_populates="recruiter"
    )

    company = relationship(
        "Company",
        back_populates="recruiters"
    )

    jobs = relationship(
        "Job",
        back_populates="recruiter"
    )