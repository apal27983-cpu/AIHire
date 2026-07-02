from app.db.database import SessionLocal
from app.models.user import User
from app.core.security import get_password_hash

db = SessionLocal()

admin = (
    db.query(User)
    .filter(
        User.email == "admin@aihire.com"
    )
    .first()
)

if not admin:
    admin = User(
        full_name="Super Admin",
        email="admin@aihire.com",
        password=get_password_hash(
            "Admin@123"
        ),
        role="admin"
    )

    db.add(admin)
    db.commit()

    print("Admin created.")
else:
    print("Admin already exists.")