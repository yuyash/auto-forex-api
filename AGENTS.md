# API Package Guide

`api` is the server-side Web API process for AutoForexV2.

## Responsibilities

- Expose HTTP endpoints for `web`.
- Treat FastAPI route metadata in this package as the source of truth for the
  frontend-facing REST contract.
- Export the generated OpenAPI schema to `openapi/openapi.yaml` after route
  changes.
- Communicate with `server` over gRPC.
- Treat `protobuf` as the source of truth for gRPC messages and services.

## Boundaries

- Do not put trading task execution or OANDA access here; that belongs in
  `server`, `core`, or `oanda`.
- Do not define `.proto` files here.
- Do not manually edit `openapi/openapi.yaml` for API behavior changes; update
  FastAPI routes here and run `uv run export-openapi`.

## Commands

```bash
uv sync
uv run auto-forex-api
uv run export-openapi
uv run ruff check .
uv run ruff format .
uv run ty check
```
