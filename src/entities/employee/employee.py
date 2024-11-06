from typing import Optional
from pydantic import BaseModel, Field
from .hard_skills import HardSkills
from .soft_skills import SoftSkills
# from uuid import UUID
# import uuid

class Employee(BaseModel):
    # uuid : UUID = uuid.uuid4()
    name: str = Field(
        min_length=6, 
        max_length=20, 
        alias="Name", 
        pattern="^[a-zA-Z]+[a-zA-Z ]*$", 
        title="Name",
        description="The name has to be a valid employee name"
                        )
    password: str = Field(
        min_length=8,
        max_length=20,
        alias="Password",
        # pattern="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,20}$",
        title="Password",
        description="The password has to be a valid password with uppercase, lowercase, number, and special characters (@$!%*?&)"
    )
    email: str #EmailStr
    phone: Optional[str] # PhoneNumber
    address: str
    department_id: int
    position_id: int
    workload: int = Optional(Field(
        ge=0, 
        lt=100,
        alias="Workload", 
        description="The workload has to be a valid workload (1-100).",
    ))
    salary: float = Optional(Field(
        gt=0, 
        lt=100000,
        alias="Salary", 
        description="The salary has to be a valid salary (xxxxxx.xx)",
    ))
    # soft_skills: Optional[list[SoftSkills]] = []
    # hard_skills: Optional[list[HardSkills]] = []  
    
    class Config:
        from_attributes=True

        
    
    
class EmployeeUpdate(BaseModel):
    id: int 
    name: str
    password: str
    email: str #EmailStr
    phone: Optional[str] # PhoneNumber
    address: str
    department_id: int
    position_id: int
    salary: float
    # soft_skills: list[SoftSkills] = []
    # hard_skills: list[HardSkills] = []
    
    class Config:
        from_attributes=True