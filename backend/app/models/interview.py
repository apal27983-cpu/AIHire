from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime
)
from sqlalchemy.orm import relationship

from app.db.base import Base


class Interview(Base):
    __tablename__ = "interviews"

    id = Column(Integer, primary_key=True, index=True)

    application_id = Column(
        Integer,
        ForeignKey("applications.id"),
        nullable=False
    )

    scheduled_at = Column(
        DateTime(timezone=True)
    )

    meeting_link = Column(String)

    status = Column(
        String,
        default="SCHEDULED"
    )

    feedback = Column(String)

    application = relationship(
        "Application",
        back_populates="interviews"
    )