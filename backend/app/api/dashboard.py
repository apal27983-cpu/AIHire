from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.api.dependencies import (
    get_current_user
)
from app.models.user import User

from app.schemas.dashboard import (
    RecruiterDashboardResponse
)

from app.services.dashboard_service import (
    get_recruiter_dashboard
)

from app.schemas.dashboard import (
    RecruiterDashboardResponse,
    CandidateDashboardResponse
)

from app.services.dashboard_service import (
    get_recruiter_dashboard,
    get_candidate_dashboard
)

#Admin Dashboard
from app.schemas.dashboard import (
    RecruiterDashboardResponse,
    CandidateDashboardResponse,
    AdminDashboardResponse
)

from app.services.dashboard_service import (
    get_recruiter_dashboard,
    get_candidate_dashboard,
    get_admin_dashboard
)

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get(
    "/recruiter",
    response_model=
    RecruiterDashboardResponse
)
def recruiter_dashboard(
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):
    try:
        if current_user.role != "recruiter":
            raise HTTPException(
                status_code=403,
                detail=
                "Only recruiters allowed"
            )

        return get_recruiter_dashboard(
            db,
            current_user.id
        )

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
    

#Candidate Dashboard
@router.get(
    "/candidate",
    response_model=
    CandidateDashboardResponse
)
def candidate_dashboard(
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):
    try:
        if current_user.role != "candidate":
            raise HTTPException(
                status_code=403,
                detail=
                "Only candidates allowed"
            )

        return get_candidate_dashboard(
            db,
            current_user.id
        )

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
    

#Admin Dashboard
@router.get(
    "/admin",
    response_model=
    AdminDashboardResponse
)
def admin_dashboard(
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):
    try:
        if current_user.role != "admin":
            raise HTTPException(
                status_code=403,
                detail=
                "Only admins allowed"
            )

        return get_admin_dashboard(
            db
        )

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )