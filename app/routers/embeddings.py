from fastapi import APIRouter, Depends
from numpy.typing import NDArray
from sentence_transformers import SentenceTransformer
from typing import Annotated
import numpy as np

from app.dependencies import get_embedding_model, get_api_key
from app.schemas import Document, Embedding

router = APIRouter(tags=["embeddings"])


@router.post("/one", response_model=Embedding)
async def create_embedding(
    document: Document,
    model: Annotated[SentenceTransformer, Depends(get_embedding_model)],
    _api_key: Annotated[str, Depends(get_api_key)],
):
    embedding: NDArray[np.floating] = model.encode_document(  # type: ignore
        sentences=document.content,
        convert_to_numpy=True,
    )

    return Embedding(
        meta=document.meta,
        embedding=embedding.tolist(),
    )


@router.post("/many", response_model=list[Embedding])
async def create_embeddings(
    documents: list[Document],
    model: Annotated[SentenceTransformer, Depends(get_embedding_model)],
    _api_key: Annotated[str, Depends(get_api_key)],
):
    sentences = list(doc.content for doc in documents)
    embeddings: NDArray[np.floating] = model.encode_document(  # type: ignore
        sentences=sentences,
        batch_size=100,
        convert_to_numpy=True,
    )

    return list(
        Embedding(
            meta=doc.meta,
            embedding=emb,
        )
        for emb, doc in zip(embeddings, documents)
    )
