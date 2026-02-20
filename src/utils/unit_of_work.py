from abc import ABC, abstractmethod

from database.core import LocalSession
from database.repositories import MessageRepository


class IUnitOfWork(ABC):
    messages: MessageRepository

    @abstractmethod
    async def __aenter__(self):
        pass

    async def __aexit__(self):
        pass

    async def rollback(self):
        pass

    async def commit(self):
        pass


class UnitOfWork(IUnitOfWork):
    def __init__(self):
        self.session_factory = LocalSession

    async def __aenter__(self):
        self.session = self.session_factory()
        self.messages = MessageRepository(self.session)

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            await self.rollback()

        await self.session.close()

    async def rollback(self):
        await self.session.rollback()

    async def commit(self):
        await self.session.commit()
