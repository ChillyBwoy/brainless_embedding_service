from pydantic import BaseModel


class Embedding(BaseModel):
    content: list[float]
