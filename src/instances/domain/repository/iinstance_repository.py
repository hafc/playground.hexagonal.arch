from abc import ABC, abstractmethod
import uuid

from domain.models.instance import Instance


class IInstanceRepository(ABC):
    @abstractmethod
    def get(self, instance_id: uuid) -> Instance:
        pass

    @abstractmethod
    def get_by(self, customer_id: uuid) -> Instance:
        pass

    @abstractmethod
    def save(self, instance: Instance) -> None:
        pass