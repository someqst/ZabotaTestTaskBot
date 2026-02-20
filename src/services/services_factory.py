from services.ai_service import AIService
from services.message_service import MessageService
from utils.unit_of_work import UnitOfWork


class ServicesFactory:
    def __init__(self):
        self._uow = UnitOfWork()
        self._message_service: MessageService = None
        self._ai_service: AIService = None

    @property
    def message(self):
        if not self._message_service:
            self._message_service = MessageService(self._uow)
        return self._message_service
    
    @property
    def ai(self):
        if not self._ai_service:
            self._ai_service = AIService()
        return self._ai_service
