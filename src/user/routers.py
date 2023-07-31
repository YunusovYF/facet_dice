# from typing import Annotated

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends

# from .dependencies import user_service
from .schemas import UserSchemaAdd
from .services import UserService

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.post('/')
@inject
async def add_user(
        user: UserSchemaAdd,
        user_service: UserService = Depends(Provide['user_service']),
):
    user_id = await user_service.add_user(user)
    return {'user_id': user_id}


@router.get('/')
@inject
async def get_users(
        user_service: UserService = Depends(Provide['user_service']),
):
    users = await user_service.get_users()
    return users

#
# @router.post("")
# async def add_user(
#         user: UserSchemaAdd,
#         users_service: Annotated[UserService, Depends(user_service)],
# ):
#     user_id = await users_service.add_user(user)
#     return {"user_id": user_id}
#
#
# @router.get("")
# async def get_users(
#         users_service: Annotated[UserService, Depends(user_service)],
# ):
#     users = await users_service.get_users()
#     return users
