from functools import lru_cache
from fastapi import Depends
from sentence_transformers import SentenceTransformer
from typing import Annotated

from app.config import Settings


@lru_cache
def get_settings() -> Settings:
    return Settings()


def _get_embedding_model(settings: Settings) -> SentenceTransformer:
    return SentenceTransformer(
        settings.model_name,
        cache_folder=settings.cache_folder,
        token=settings.hf_token,
    )


@lru_cache
def get_embedding_model(
    settings: Annotated[Settings, Depends(get_settings)],
) -> SentenceTransformer:
    return _get_embedding_model(settings)
