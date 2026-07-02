from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.company import (
    CompanyCreate,
    CompanyResponse
)
from app.services.company_service import (
    create_new_company,
    get_company
)

router = APIRouter(
    prefix="/company",
    tags=["Company"]
)


@router.post(
    "",
    response_model=CompanyResponse
)
def create_company(
    request: CompanyCreate,
    db: Session = Depends(get_db)
):
    try:
        return create_new_company(
            db,
            request.name,
            request.website,
            request.industry,
            request.location
        )

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get(
    "/{company_id}",
    response_model=CompanyResponse
)
def get_company_by_id(
    company_id: int,
    db: Session = Depends(get_db)
):
    try:
        return get_company(
            db,
            company_id
        )

    except Exception as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )