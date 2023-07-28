from uuid import UUID

from pydantic import BaseModel


class UserSchema(BaseModel):
    id: UUID
    username: str

    class Config:
        from_attributes = True


class UserSchemaAdd(BaseModel):
    username: str
    password: str
