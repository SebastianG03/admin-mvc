from pydantic import BaseModel, Field


class Department(BaseModel):
    # id: str
    name: str = Field(
        min_length=3,
        max_length=55,
        alias="Name",
        pattern="^[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ'’-]+(?: [a-zA-ZáéíóúÁÉÍÓÚñÑüÜ'’-]+)*$",
        title="Name",
        description="The name has to be a valid department name",
    )
    location: str = Field(
        min_length=3,
        max_length=95,
        alias="Location",
        title="Location",
        description="The location has to be a valid location",
    )
    
    class Config:
        arbitrary_types_allowed = True
        from_attributes = True
        populate_by_name = True