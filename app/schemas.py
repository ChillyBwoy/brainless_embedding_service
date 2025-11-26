from typing import Any
from pydantic import BaseModel


class Document(BaseModel):
    meta: dict[str, Any]
    content: str


class Embedding(BaseModel):
    meta: dict[str, Any]
    embedding: list[float]


class Prompt(BaseModel):
    content: str


class Message(BaseModel):
    content: str
    thinking: str
