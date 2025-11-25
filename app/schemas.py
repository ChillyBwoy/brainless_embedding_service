from typing import Any
from pydantic import BaseModel


class Document(BaseModel):
    content: str
    meta: dict[str, Any]


class Embedding(BaseModel):
    content: list[float]
    meta: dict[str, Any]


class Prompt(BaseModel):
    content: str


class Message(BaseModel):
    content: str
    thinking: str
