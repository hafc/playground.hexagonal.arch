from abc import ABC, abstractmethod
from domain.dto.instance_dto import CreateInstanceDto
import uuid


class IInstanceService(ABC):
    @abstractmethod
    async def create(self, create_instance_dto: CreateInstanceDto):
        pass

    @abstractmethod
    async def update_flavor(self, instance_id: uuid, flavor_id: uuid):
        pass

    @abstractmethod
    async def start(self, instance_id: uuid):
        pass

    @abstractmethod
    async def stop(self, instance_id: uuid):
        pass

    @abstractmethod
    async def delete(self, instance_id: uuid):
        pass