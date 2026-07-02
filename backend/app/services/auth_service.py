from sqlalchemy.orm import Session

from app.repositories.user_repository import (
    get_user_by_email,
    create_user
)

from app.core.security import (
    hash_password,
    verify_password,
    create_access_token
)


def register_user(
    db: Session,
    full_name: str,
    email: str,
    password: str,
    role: str
):
    # Only public roles allowed
    allowed_roles = [
        "candidate",
        "recruiter"
    ]

    role = role.lower().strip()

    if role not in allowed_roles:
        raise Exception(
            "Invalid role. Only candidate and recruiter registration is allowed."
        )

    existing_user = get_user_by_email(
        db,
        email
    )

    if existing_user:
        raise Exception(
            "Email already registered"
        )

    hashed_password = hash_password(
        password
    )

    user = create_user(
        db,
        full_name,
        email,
        hashed_password,
        role
    )

    return user


def login_user(
    db: Session,
    email: str,
    password: str
):
    user = get_user_by_email(
        db,
        email
    )

    if not user:
        raise Exception(
            "Invalid credentials"
        )

    if not verify_password(
        password,
        user.password
    ):
        raise Exception(
            "Invalid credentials"
        )

    token = create_access_token(
        {
            "sub": str(user.id),
            "role": user.role
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }