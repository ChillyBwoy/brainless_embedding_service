FROM ghcr.io/astral-sh/uv:python3.14-trixie AS builder

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

COPY . /brainless

WORKDIR /brainless

RUN uv sync --locked

FROM ghcr.io/astral-sh/uv:python3.14-trixie-slim AS runtime

ARG MODEL_NAME
ARG HF_TOKEN
ARG API_KEY

ENV PATH="/brainless/.venv/bin:$PATH" \
    PYTHONIOENCODING=utf-8 \
    PYTHONUNBUFFERED=1 \
    DEBUG=false \
    OPENAPI_URL=/openapi.json \
    CACHE_FOLDER=/brainless/.models

WORKDIR /brainless

COPY . /brainless
COPY --from=builder /brainless/.venv /brainless/.venv

EXPOSE 8000
CMD ["fastapi", "run", "app/main.py", "--port", "8000"]
