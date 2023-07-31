from dependency_injector import containers, providers

from src.user.repositories import UserRepository
from src.user.services import UserService


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=[
        "src.user.routers",
    ])

    user_service = providers.Factory(
        UserService,
        user_repository=UserRepository
    )
