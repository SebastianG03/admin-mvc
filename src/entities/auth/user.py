from pydantic import BaseModel, EmailStr, Field
from entities.employee.employee import EmployeeUpdate
from entities.auth.token import Token, TokenData

class User(BaseModel):
    user_data: EmployeeUpdate
    token: Token | None = None
    # toke_data: TokenData
    disabled: bool | None = None
    
    class Config:
        from_attributes=True
        arbitrary_types_allowed=True
        
    
class LoginModel(BaseModel):
    email: EmailStr = Field(
        title= "Email",
        alias= "Email",
        description= "Write the employee email"
    )
    password: str = Field(
        min_length=8, 
        max_length=20, 
        alias="Password", 
        title="Password",
        description="Write a valid password between 8 and 20 characters"
        )
    
    class Config:
        from_attributes=True
        arbitrary_types_allowed=True
    