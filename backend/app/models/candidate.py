from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base


class Candidate(Base):
    __tablename__ = "candidates"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    phone = Column(String)
    experience = Column(Integer)
    current_location = Column(String)
    preferred_location = Column(String)
    skills = Column(String)
    resume_url = Column(String)

    user = relationship(
        "User",
        back_populates="candidate"
    )

    applications = relationship(
        "Application",
        back_populates="candidate"
    )