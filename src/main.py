from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.config.container import Container
from src.config.routers import all_routers


def create_app() -> FastAPI:
    container = Container()

    app = FastAPI()

    origins = [
        'http://localhost:8000'
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )

    app.container = container

    for router in all_routers:
        app.include_router(router)

    return app


app = create_app()
