from functools import lru_cache
from fastapi import Depends, Security, HTTPException, status
from fastapi.security import APIKeyHeader
from sentence_transformers import SentenceTransformer
from typing import Annotated

from app.config import Settings

api_key_header = APIKeyHeader(name="X-API-Key", auto_error=True)


@lru_cache
def get_settings() -> Settings:
    return Settings()


def _get_embedding_model(settings: Settings) -> SentenceTransformer:
    return SentenceTransformer(
        settings.embedding_model,
        cache_folder=settings.embedding_cache_folder,
        token=settings.hf_token,
    )


@lru_cache
def get_embedding_model(
    settings: Annotated[Settings, Depends(get_settings)],
) -> SentenceTransformer:
    return _get_embedding_model(settings)


def get_api_key(
    api_key: Annotated[str, Security(api_key_header)],
    settings: Annotated[Settings, Depends(get_settings)],
):
    if api_key != settings.api_key:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid API Key",
        )
    return api_key
