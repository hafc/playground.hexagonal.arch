import uuid
from kink import inject
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from application.iinstance_service import IInstanceService
from domain.dto.instance_dto import CreateInstanceDto

router = APIRouter()

@inject
class InstanceController:
    def __init__(self, instance_service: IInstanceService) -> None:
        self._instance_service = instance_service


    @router.post(
        "/instance",
         responses={400: {"model": "Dados invalidos"}, 500: {"model": "Falha na criacao da instancia"}},
    )
    async def create_instance(self, request: CreateInstanceDto) -> JSONResponse:
        result = self._instance_service.create(request)
        return JSONResponse(content=result.dict(), status_code=status.HTTP_201_CREATED)

    @router.put(
        "/instances/{instance_id}/flavor/{flavor_id}",
        responses={400: "Dados invalidos", 404: "Instancia nao localizada", 500: "Falha na criacao de instancia"},
        tags=["gym_passes"],
    )
    async def update_flavor(self, instance_id: uuid, flavor_id: uuid) -> JSONResponse:
        result = self._instance_service.update_flavor(instance_id, flavor_id)
        return JSONResponse(content=result.dict(), status_code=status.HTTP_200_OK)
