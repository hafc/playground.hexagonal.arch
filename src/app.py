from typing import Any

import uvicorn
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from instances.entrypoints.api.instance_controller import InstanceController

app = FastAPI()
app.include_router(InstanceController.router)


def custom_openapi() -> dict[str, Any]:
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="Hexagonal-Architecture",
        version="1.0.0",
        description="Hexagonal architecture in Python",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema

    return app.openapi_schema 


app.openapi = custom_openapi

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=5000)