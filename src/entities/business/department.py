from pydantic import BaseModel


class Department(BaseModel):
    # id: str
    name: str
    location: str