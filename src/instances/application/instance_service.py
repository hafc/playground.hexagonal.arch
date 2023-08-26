import uuid
from kink import inject
from domain.repository.iinstance_repository import IInstanceRepository
from domain.models.instance import Instance

@inject
class InstanceService:
    def __init__(self, instance_repository: IInstanceRepository) -> None:
        self._instance_repository = instance_repository
    
    async def create(self, customer_id: uuid, flavor_id: uuid, name: str):
        instance: Instance(uuid.uuid4(), customer_id, name, flavor_id)
        await self._instance_repository.save(instance)
    
    async def update_flavor(self, instance_id: uuid, flavor_id: uuid):
        instance = await self._instance_repository.get(instance_id)

        if instance is None:
            print('Instance not found')
        
        instance.update_flavor(flavor_id)
        await self._instance_repository.save(instance)
    
    async def start(self, instance_id: uuid):
        instance = await self._instance_repository.get(instance_id)

        if instance is None:
            print('Instance not found')
        
        instance.start()
        await self._instance_repository.save(instance)
    
    async def stop(self, instance_id: uuid):
        instance = await self._instance_repository.get(instance_id)

        if instance is None:
            print('Instance not found')
        
        instance.stop()
        await self._instance_repository.save(instance)
    
    async def delete(self, instance_id: uuid):
        instance = await self._instance_repository.get(instance_id)

        if instance is None:
            print('Instance not found')
        
        instance.delete()
        await self._instance_repository.save(instance)

        
