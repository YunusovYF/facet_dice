from dependency_injector import containers, providers

from .services import UserService


class UserContainer(containers.DeclarativeContainer):
    service = providers.Factory(UserService)
