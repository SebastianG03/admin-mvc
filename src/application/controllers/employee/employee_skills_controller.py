from fastapi import APIRouter, Depends
from requests import Session
from core.database.database import get_session
import core.datasource.employee_skills_datasource as ds

employee_skills_router = APIRouter(prefix="/employee/skills", tags=["employee skills"])

#Soft user skills
@employee_skills_router.get("/soft/all")
def get_user_soft_skills(session: Session = Depends(get_session)):
    return ds.get_user_soft_skills(session)

@employee_skills_router.post("/soft/create")
def post_user_soft_skills(
    employee_id: int,
    soft_skill_id: int,
    domain: int, 
    session: Session = Depends(get_session)):
    return ds.post_user_soft_skills(employee_id=employee_id, soft_skill_id=soft_skill_id, domain=domain, session=session)

@employee_skills_router.put("/soft/update")
def update_user_soft_skills(
    employee_id: int,
    soft_skill_id: int,
    domain: int, 
    session: Session = Depends(get_session)):
    return ds.update_user_soft_skills(employee_id=employee_id, soft_skill_id=soft_skill_id, domain=domain, session=session)

#Hard user skills
@employee_skills_router.get("/hard/all")
def get_user_soft_skills(session: Session = Depends(get_session)):
    return ds.get_user_hard_skills(session)

@employee_skills_router.post("/hard/create")
def post_user_hard_skills(
    employee_id: int,
    hard_skill_id: int,
    domain: int, 
    session: Session = Depends(get_session)):
    return ds.post_user_hard_skills(employee_id=employee_id, hard_skill_id=hard_skill_id, domain=domain, session=session)

@employee_skills_router.put("/hard/update")
def update_user_hard_skills(
    employee_id: int,
    hard_skill_id: int,
    domain: int, 
    session: Session = Depends(get_session)):
    return ds.update_user_hard_skills(employee_id=employee_id, hard_skill_id=hard_skill_id, domain=domain, session=session)