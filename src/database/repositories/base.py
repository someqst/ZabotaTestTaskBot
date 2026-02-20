from sqlalchemy import delete, insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from typing import Type, TypeVar
from abc import ABC, abstractmethod


T = TypeVar("T")


class IRepository(ABC):
    @abstractmethod
    async def add_one(self):
        pass

    @abstractmethod
    async def delete_one(self):
        pass

    @abstractmethod
    async def update_one(self):
        pass

    @abstractmethod
    async def get_one(self):
        pass


class BaseRepository(IRepository):
    model: Type[T] = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_one(self, data: dict) -> T | None:
        stmt = insert(self.model).values(**data).returning(self.model)
        res = await self.session.execute(stmt)
        return res.scalar_one_or_none()

    async def delete_one(self, id: int):
        stmt = delete(self.model).where(self.model.id == id)
        await self.session.execute(stmt)

    async def update_one(self, id: int, data: dict):
        stmt = update(self.model).values(**data).where(self.model.id == id)
        await self.session.execute(stmt)

    async def get_one(self, id: int) -> T | None:
        stmt = select(self.model).where(self.model.id == id)
        res = await self.session.execute(stmt)
        return res.scalar_one_or_none()
