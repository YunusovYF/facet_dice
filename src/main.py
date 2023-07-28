import asyncio

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.config.db import init_models
from src.config.routers import all_routers

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

for router in all_routers:
    app.include_router(router)

if __name__ == "__main__":
    asyncio.run(init_models())
    print("Done")
    uvicorn.run(app="main:app", reload=True)
