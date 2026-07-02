from sqlalchemy.orm import Session
from app.models.company import Company


def create_company(
    db: Session,
    company: Company
):
    db.add(company)
    db.commit()
    db.refresh(company)
    return company


def get_company_by_id(
    db: Session,
    company_id: int
):
    return (
        db.query(Company)
        .filter(Company.id == company_id)
        .first()
    )