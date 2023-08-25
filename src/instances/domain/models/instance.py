import uuid
from datetime import date
from instances.domain.models.status import Status


class Instance:
    def __init__(self, instance_id: uuid, customer_id: uuid, name: str, flavor_id: uuid):
        self._instance_id = instance_id
        self._customer_id = customer_id
        self._name = name
        self._flavor_id = flavor_id
    
    def create(self):
        self._status = Status.creating
        self._created_at = date.today()
        self._create_by = self._customer_id
        return self
     
    def update_flavor(self, new_flavor_id):
        self._flavor_id = new_flavor_id
        self._update_at = date.today()
        self.update_by = self._customer_id
        return self
    
    def start(self):
        self._status = Status.active
        self._start_at = date.today()
        self._started_by = self._customer_id
        return self
    
    def stop(self):
        self._status = Status.stoped
        self._stoped_at = date.today()
        self._stoped_by = self._customer_id
        return self    

    def delete(self):
        self._status = Status.deleted
        self._deleted_at = date.today()
        self._deleted_by = self._customer_id
