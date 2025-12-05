from fastapi import APIRouter, Depends
from numpy.typing import NDArray
from sentence_transformers import SentenceTransformer
from typing import Annotated
import numpy as np

from app.dependencies import get_embedding_model, get_api_key
from app.schemas import Embedding, CreateEmbedding, CreateEmbeddingBulk

router = APIRouter(tags=["embeddings"])


@router.post(
    "/",
    response_model=list[float],
    dependencies=[Depends(get_api_key)],
)
async def create(
    input: CreateEmbedding,
    model: Annotated[SentenceTransformer, Depends(get_embedding_model)],
):
    embedding: NDArray[np.floating] = model.encode_document(  # type: ignore
        sentences=input.content,
        convert_to_numpy=True,
        truncate_dim=input.dimensions,
    )

    return embedding.tolist()


@router.post(
    "/bulk",
    response_model=list[Embedding],
    dependencies=[Depends(get_api_key)],
)
async def bulk(
    input: CreateEmbeddingBulk,
    model: Annotated[SentenceTransformer, Depends(get_embedding_model)],
):
    sentences = list(doc.content for doc in input.documents)
    vectors: NDArray[np.floating] = model.encode_document(  # type: ignore
        sentences=sentences,
        convert_to_numpy=True,
        truncate_dim=input.dimensions,
    )

    return list(
        Embedding(id=doc.id, vector=vector)
        for vector, doc in zip(vectors, input.documents)
    )
