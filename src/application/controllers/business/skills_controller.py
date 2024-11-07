from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from entities.employee import HardSkills, SoftSkills
from core.database.database import get_session
from core.services.user_service import user_service
import core.datasource.skills_datasource as sd


skills_router = APIRouter(prefix="/business/skills", tags=["skills"])

#Hard Skills
skills_router.post(
    "hard/create",
    status_code=status.HTTP_201_CREATED
)
def create_hard_skill(
    skill: HardSkills,
    session: Session = Depends(get_session)
):
    user = user_service.get_user()
    
    if user:
        return sd.post_hard_skills(
            skill, session
        )
    else:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            content={"message": "Unauthorized Access"})

@skills_router.get(
    "hard/all",
    status_code=status.HTTP_200_OK
)
def get_hard_skills(session: Session = Depends(get_session)):
    return sd.get_hard_skills(session)
        
@skills_router.put(
    "/hard/update/{id}",
    status_code=status.HTTP_202_ACCEPTED
)
def update_hard_skill(
    id: int,
    skill: HardSkills,
    session: Session = Depends(get_session)
):
    user = user_service.get_user()
    
    if user and user.is_admin:
        return sd.update_hard_skills(id, skill, session)
    else:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            content={"message": "Unauthorized Access"})

#Soft Skills

skills_router.post(
    "/soft/create",
    status_code=status.HTTP_201_CREATED
)
def create_soft_skill(
    skill: SoftSkills,
    session: Session = Depends(get_session)
):
    user = user_service.get_user()
    
    if user:
        return sd.post_soft_skills(
            skill, session
        )
    else:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            content={"message": "Unauthorized Access"})

@skills_router.get(
    "/soft/all",
    status_code=status.HTTP_200_OK
)
def get_soft_skills(session: Session = Depends(get_session)):
    return sd.get_soft_skills(session)
        
@skills_router.put(
    "/soft/update/{id}",
    status_code=status.HTTP_202_ACCEPTED
)
def update_soft_skill(
    id: int,
    skill: SoftSkills,
    session: Session = Depends(get_session)
):
    user = user_service.get_user()
    
    if user and user.is_admin:
        return sd.update_soft_skills(id, skill, session)
    else:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            content={"message": "Unauthorized Access"})
