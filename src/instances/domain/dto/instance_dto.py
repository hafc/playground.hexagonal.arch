import uuid

class CreateInstanceDto:
     def __init__(self, customer_id: uuid, name: str, flavor_id: uuid):
        self._customer_id = customer_id
        self._name = name
        self._flavor_id = flavor_id