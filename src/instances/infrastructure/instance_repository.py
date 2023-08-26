import copy
import uuid
from domain.repository.iinstance_repository import IInstanceRepository
from domain.models.instance import Instance


class InstanceRepository(IInstanceRepository):
    def __init__(self) -> None:
        self._instances: dict[uuid.UUID, Instance] = {}

    def get(self, instance_id: uuid.uuid4) -> Instance:
        try:
            return copy.deepcopy(self._instances[instance_id])
        except KeyError as error:
            print('error')

    def get_all(self) -> list[Instance]:
        instances = []
        for instance in self._instances.values():
            instances.append(copy.deepcopy(instance))
        return instances

    def save(self, instance: Instance) -> None:
        self._instances[instance._instance_id] = copy.deepcopy(instance)