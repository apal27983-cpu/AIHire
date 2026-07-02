from fastapi import FastAPI
from sqlalchemy import text

from app.db.database import engine
from app.db.base import Base
import app.models

from app.api.auth import router as auth_router
from app.api.candidate import router as candidate_router
from app.api.company import router as company_router
from app.api.recruiter import router as recruiter_router
from app.api.job import router as job_router
from app.api.application import (
    router as application_router
)
from app.api.interview import router as interview_router
from app.api.dashboard import (
    router as dashboard_router
)

app = FastAPI(
    title="AIHire API",
    version="1.0.0"
)

app.include_router(auth_router)
app.include_router(candidate_router)
app.include_router(company_router)
app.include_router(recruiter_router)
app.include_router(job_router)
app.include_router(
    application_router
)
app.include_router(interview_router)
app.include_router(
    dashboard_router
)


@app.get("/")
def root():
    return {"message": "AIHire API Running"}


@app.get("/db-test")
def db_test():
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))

    return {"message": "Database Connected Successfully"}