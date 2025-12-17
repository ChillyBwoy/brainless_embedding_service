from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.dependencies import get_settings
from app.routers.embeddings import router as embeddings_router
from app.routers.reranking import router as reranking_router

settings = get_settings()

app = FastAPI(
    debug=settings.debug,
    openapi_url=settings.openapi_url,
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allow_origins,
    allow_credentials=settings.allow_credentials,
    allow_methods=settings.allow_methods,
    allow_headers=settings.allow_headers,
)

app.include_router(embeddings_router, prefix="/api/embeddings")
app.include_router(reranking_router, prefix="/api/reranking")
