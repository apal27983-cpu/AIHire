from sqlalchemy.orm import Session

from app.models.company import Company
from app.repositories.company_repository import (
    create_company,
    get_company_by_id
)


def create_new_company(
    db: Session,
    name: str,
    website: str,
    industry: str,
    location: str
):
    company = Company(
        name=name,
        website=website,
        industry=industry,
        location=location
    )

    return create_company(
        db,
        company
    )


def get_company(
    db: Session,
    company_id: int
):
    company = get_company_by_id(
        db,
        company_id
    )

    if not company:
        raise Exception("Company not found")

    return company