from fastapi import APIRouter
import numpy as np
from numpy.typing import NDArray
from sentence_transformers import SentenceTransformer


from core.config import get_settings
from schemas.document import Document
from schemas.embedding import Embedding


router = APIRouter(tags=["embeddings"])

settings = get_settings()
model = SentenceTransformer(
    settings.embedding_model_name,
    cache_folder=settings.cache_folder,
    token=settings.hf_token,
)


@router.post("/one", response_model=Embedding)
async def create_embedding(document: Document):
    embedding: NDArray[np.floating] = model.encode_document(  # type: ignore
        sentences=document.content,
        convert_to_numpy=True,
    )

    return Embedding(content=embedding.tolist())


@router.post("/many", response_model=list[Embedding])
async def create_embeddings(documents: list[Document]):
    sentences = list(doc.content for doc in documents)
    embeddings: NDArray[np.floating] = model.encode_document(  # type: ignore
        sentences=sentences,
        batch_size=100,
        convert_to_numpy=True,
    )

    return list(Embedding(content=embedding) for embedding in embeddings)
