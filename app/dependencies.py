from functools import lru_cache
from fastapi import Depends
from sentence_transformers import SentenceTransformer
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    PreTrainedTokenizer,
    PreTrainedModel,
)
from typing import Annotated

from app.config import Settings


@lru_cache
def get_settings() -> Settings:
    return Settings()


def _get_embedding_model(settings: Settings) -> SentenceTransformer:
    return SentenceTransformer(
        settings.embedding_model_name,
        cache_folder=settings.cache_folder,
        token=settings.hf_token,
    )


@lru_cache
def get_embedding_model(
    settings: Annotated[Settings, Depends(get_settings)],
) -> SentenceTransformer:
    return _get_embedding_model(settings)


def _get_tokenizer(settings: Settings) -> PreTrainedTokenizer:
    return AutoTokenizer.from_pretrained(
        settings.prediction_model_name,
        cache_dir=settings.cache_folder,
        token=settings.hf_token,
    )


@lru_cache
def get_tokenizer(
    settings: Annotated[Settings, Depends(get_settings)],
) -> PreTrainedTokenizer:
    return _get_tokenizer(settings)


def _get_prediction_model(settings: Settings) -> PreTrainedModel:
    return AutoModelForCausalLM.from_pretrained(
        settings.prediction_model_name,
        cache_dir=settings.cache_folder,
        token=settings.hf_token,
        torch_dtype="auto",
        device_map="auto",
    )


@lru_cache
def get_prediction_model(
    settings: Annotated[Settings, Depends(get_settings)],
) -> PreTrainedModel:
    return _get_prediction_model(settings)
