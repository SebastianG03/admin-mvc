from pydantic import BaseModel


class Position(BaseModel):
    # id: int
    name: str