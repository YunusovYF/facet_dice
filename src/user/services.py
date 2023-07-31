from typing import List
from uuid import UUID

from src.core.repositories import AbstractRepository
from .schemas import UserSchemaAdd, UserSchema


class UserService:
    def __init__(self, user_repository: AbstractRepository) -> None:
        self.user_repository: AbstractRepository = user_repository()

    async def add_user(self, user: UserSchemaAdd) -> UUID:
        user_dict = user.model_dump()
        user_id = await self.user_repository.add_one(user_dict)
        return user_id

    async def get_users(self) -> List[UserSchema]:
        users = await self.user_repository.find_all()
        return users
