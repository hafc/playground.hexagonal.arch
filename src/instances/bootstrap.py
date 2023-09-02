from kink import di
from domain.repository.iinstance_repository import IInstanceRepository
from infrastructure.instance_repository import InstanceRepository
from application.iinstance_service import IInstanceService
from application.instance_service import InstanceService


def bootstrap_di() -> None:
    repository = InstanceRepository()
    service = InstanceService(repository)

    di[IInstanceRepository] = repository
    di[IInstanceService] = service