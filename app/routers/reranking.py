from fastapi import APIRouter, Depends
from typing import Annotated

from google.cloud import discoveryengine

from app.config import Settings
from app.dependencies import get_api_key, get_settings
from app.schemas import Document, RerankBulk, RankedDocument


router = APIRouter(tags=["reranking"])


def _prepare_documents(
    documents: list[Document],
) -> list[discoveryengine.RankingRecord]:
    result: list[discoveryengine.RankingRecord] = []

    for doc in documents:
        result.append(
            discoveryengine.RankingRecord(
                id=doc.id,
                content=doc.content,
            )
        )

    return result


@router.post(
    "/bulk",
    response_model=list[RankedDocument],
    dependencies=[Depends(get_api_key)],
)
async def rerank(
    data: RerankBulk,
    settings: Annotated[Settings, Depends(get_settings)],
):
    client = discoveryengine.RankServiceAsyncClient()
    ranking_config = client.ranking_config_path(
        project=settings.vertex_ai_project_id,
        location=settings.vertex_ai_location,
        ranking_config="default_ranking_config",
    )
    request = discoveryengine.RankRequest(
        ranking_config=ranking_config,
        model=settings.vertex_ai_model,
        top_n=data.n,
        query=data.query,
        records=_prepare_documents(data.documents),
    )

    response = await client.rank(request=request)

    docs: list[RankedDocument] = []

    for rec in response.records:
        docs.append(RankedDocument(id=rec.id, score=rec.score))

    return docs
