from app.auth.repository import UserRepository
from app.auth.schemas import UserLogin, UserRegister
from app.auth.security import (
    create_access_token,
    hash_password,
    verify_password,
)
from app.models.user import User


class AuthService:
    """Business logic for authentication."""

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def register(self, data: UserRegister) -> User:
        existing_user = self.repository.get_by_email(data.email)

        if existing_user:
            raise ValueError("Email already registered")

        hashed_password = hash_password(data.password)

        return self.repository.create(
            full_name=data.full_name,
            email=data.email,
            hashed_password=hashed_password,
        )

    def login(self, data: UserLogin) -> str:
        user = self.repository.get_by_email(data.email)

        if user is None:
            raise ValueError("Invalid email or password")

        if not verify_password(
            data.password,
            user.hashed_password,
        ):
            raise ValueError("Invalid email or password")

        return create_access_token(subject=str(user.id))