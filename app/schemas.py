from typing import Annotated
from pydantic import BaseModel, BeforeValidator

SUPPORTED_DIMENSIONS = [128, 256, 512, 768, 1024]


def validate_dimension(dimensions: int) -> int:
    if dimensions not in SUPPORTED_DIMENSIONS:
        raise ValueError(
            f"Invalid dimension. Supported dimensions are: {SUPPORTED_DIMENSIONS}"
        )
    return dimensions


class Document(BaseModel):
    """
    Base input data
    """

    id: str | int
    content: str


class Embedding(BaseModel):
    """
    Output data
    """

    id: str | int
    vector: list[float]


class CreateEmbedding(BaseModel):
    """
    Single embed payload
    """

    content: str
    dimensions: Annotated[int, BeforeValidator(validate_dimension)]


class CreateEmbeddingBulk(BaseModel):
    """
    Multiple embed payload
    """

    documents: list[Document]
    dimensions: Annotated[int, BeforeValidator(validate_dimension)]
