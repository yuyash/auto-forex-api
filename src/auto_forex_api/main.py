from typing import Literal

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict


class HealthResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    status: Literal["ok"]


app = FastAPI(
    title="AutoForex API",
    version="0.1.0",
    license_info={"name": "Apache-2.0", "identifier": "Apache-2.0"},
    servers=[{"url": "http://127.0.0.1:8001"}],
)


@app.get(
    "/api/health",
    operation_id="getHealth",
    response_model=HealthResponse,
    responses={400: {"description": "Invalid request."}},
    summary="Get API health status",
    tags=["system"],
    openapi_extra={"security": []},
)
def health() -> HealthResponse:
    return HealthResponse(status="ok")


def main() -> None:
    uvicorn.run("auto_forex_api.main:app", host="127.0.0.1", port=8001)
