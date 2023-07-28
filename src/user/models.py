from uuid import UUID

from sqlalchemy.orm import Mapped, mapped_column

from src.config.db import Base
from .schemas import UserSchema


class User(Base):
    __tablename__ = 'users'

    id: Mapped[UUID] = mapped_column(primary_key=True)
    username: Mapped[str]
    password: Mapped[str]

    def to_read_model(self) -> UserSchema:
        return UserSchema(
            id=self.id,
            username=self.username
        )
