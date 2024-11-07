from fastapi import APIRouter, Depends
from requests import Session
from core.database.database import get_session
import core.datasource.employee_skills_datasource as ds
from core.services.user_service import user_service
from entities.auth.user import User

employee_skills_router = APIRouter(prefix="/employee/skills", tags=["employee skills"])

#Soft user skills
@employee_skills_router.get("/soft/all")
def get_user_soft_skills(session: Session = Depends(get_session)):
    user: User = user_service.get_user()
    if user:
        return ds.get_user_soft_skills(employee_id= user.user_data.id, session=session)
    return JSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED, 
        content={"message": "Unauthorized Access"})

@employee_skills_router.post("/soft/create")
def post_user_soft_skills(
    soft_skill_id: int,
    domain: int, 
    session: Session = Depends(get_session)):
    user: User = user_service.get_user()
    if user:
        return ds.post_user_soft_skills(
            employee_id=user.user_data.id, 
            soft_skill_id=soft_skill_id, 
            domain=domain, 
            session=session)
    return JSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED, 
        content={"message": "Unauthorized Access"})

@employee_skills_router.put("/soft/update")
def update_user_soft_skills(
    soft_skill_id: int,
    domain: int, 
    session: Session = Depends(get_session)):
    user: User = user_service.get_user()
    if user:
        return ds.update_user_soft_skills(
            employee_id=user.user_data.id,
            soft_skill_id=soft_skill_id,
            domain=domain, session=session)
    return JSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED, 
        content={"message": "Unauthorized Access"})

#Hard user skills
@employee_skills_router.get("/hard/all")
def get_user_soft_skills(session: Session = Depends(get_session)):
    user: User = user_service.get_user()
    if user:
        return ds.get_user_hard_skills(employee_id= user.user_data.id, session=session)
    return JSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED, 
        content={"message": "Unauthorized Access"})

@employee_skills_router.post("/hard/create")
def post_user_hard_skills(
    hard_skill_id: int,
    domain: int, 
    session: Session = Depends(get_session)):
    user: User = user_service.get_user()
    if user:
        return ds.post_user_hard_skills(
            employee_id=user.user_data.id, 
            hard_skill_id=hard_skill_id, 
            domain=domain, 
            session=session)
    return JSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED, 
        content={"message": "Unauthorized Access"})

@employee_skills_router.put("/hard/update")
def update_user_hard_skills(
    hard_skill_id: int,
    domain: int, 
    session: Session = Depends(get_session)):
    user: User = user_service.get_user()
    if user:
        return ds.update_user_hard_skills(
            employee_id=user.user_data.id, 
            hard_skill_id=hard_skill_id, 
            domain=domain, 
            session=session)
    return JSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED, 
        content={"message": "Unauthorized Access"})