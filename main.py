from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.embeddings import router as embeddings_router
from routes.predictions import router as predictions_router
from core.config import get_settings

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
app.include_router(predictions_router, prefix="/api/predictions")
