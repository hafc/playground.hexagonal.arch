from abc import ABC, abstractmethod
import uuid

from domain.models.instance import Instance


class IInstanceRepository(ABC):
    @abstractmethod
    async def get(self, instance_id: uuid) -> Instance:
        pass

    @abstractmethod
    async def get_by(self, customer_id: uuid) -> Instance:
        pass

    @abstractmethod
    async def save(self, instance: Instance) -> None:
        pass