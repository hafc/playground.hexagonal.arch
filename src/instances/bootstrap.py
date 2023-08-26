from kink import di
from domain.repository.iinstance_repository import IInstanceRepository
from infrastructure.instance_repository import InstanceRepository

def bootstrap_di() -> None:
    repository = InstanceRepository()

    di[IInstanceRepository] = repository