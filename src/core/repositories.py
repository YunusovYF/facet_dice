from abc import ABC, abstractmethod
from uuid import UUID

from sqlalchemy import select, insert

from src.config.db import async_session_maker


class AbstractRepository(ABC):
    model = None

    def __call__(self):
        pass

    @abstractmethod
    async def add_one(self, values: dict):
        raise NotImplementedError

    @abstractmethod
    async def find_all(self):
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def add_one(self, values: dict) -> UUID:
        async with async_session_maker() as session:
            stmt = insert(self.model).values(**values).returning(self.model.id)
            res = await session.execute(stmt)
            await session.commit()
            return res.scalar_one()

    async def find_all(self):
        async with async_session_maker() as session:
            query = select(self.model)
            res = await session.execute(query)
            res = [row[0].to_read_model() for row in res.all()]
            return res
