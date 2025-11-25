from typing import Any
from pydantic import BaseModel


class Document(BaseModel):
    content: str
    meta: dict[str, Any]


class DocumentWithEmbedding(Document):
    embedding: list[float]


class Prompt(BaseModel):
    content: str


class Message(BaseModel):
    content: str
    thinking: str
