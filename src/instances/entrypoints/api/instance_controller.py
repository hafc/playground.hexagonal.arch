import uuid
from kink import inject
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from instances.application.iinstance_service import IInstanceService
from instances.domain.dto.instance_dto import CreateInstanceDto

router = APIRouter()

@inject
class InstanceController:
    def __init__(self, instance_service: IInstanceService) -> None:
        self._instance_service = instance_service

    @router.post(
        "/instance", 
        response_model=None
    )
    async def create_instance(self, request: CreateInstanceDto) -> JSONResponse:
        result = self._instance_service.create(request)
        return JSONResponse(content=result.dict(), status_code=status.HTTP_201_CREATED)

    @router.put(
        "/instances/{instance_id}/flavor/{flavor_id}",
        response_model=None
    )
    async def update_flavor(self, instance_id: uuid, flavor_id: uuid) -> JSONResponse:
        result = self._instance_service.update_flavor(instance_id, flavor_id)
        return JSONResponse(content=result.dict(), status_code=status.HTTP_200_OK)
