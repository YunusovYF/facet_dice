from src.core.repositories import SQLAlchemyRepository
from .models import User


class UserRepository(SQLAlchemyRepository):
    model = User
