from pydantic import BaseModel, Field


class Position(BaseModel):
    # id: int
    name: str = Field(
        min_length=5,
        max_length=40,
        alias="Name",
        pattern="^[a-zA-Z]+[a-zA-Z ]*$",
        title="Name",
        description="The name has to be a valid position name",
    )
    
    class Config:
        arbitrary_types_allowed = True
        from_attributes = True
        populate_by_name = True