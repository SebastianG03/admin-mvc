from typing import List
from fastapi import HTTPException
from sqlalchemy import Sequence
from sqlalchemy.orm import Session

from entities.tables.skills_tables import HardSkillsModel, SoftSkillsModel
from entities.tables.employee_skills_tables import EmployeeHardSkillsModel, EmployeeSoftSkillsModel
from entities.employee.ablilities import EmployeeAbility

from core.services.logger_service import logger
from core.datasource.skills_datasource import get_hard_skills_by_ids, get_soft_skills_by_ids

### User Skills table

def get_user_soft_skills(
    employee_id: int, 
    session: Session) -> List[EmployeeSoftSkillsModel]:
    result = session.query(EmployeeSoftSkillsModel).where(
        EmployeeSoftSkillsModel.employee_id == employee_id).all()
    return result

def get_user_hard_skills(
    employee_id: int, 
    session: Session) -> List[EmployeeHardSkillsModel]:
    result = session.query(EmployeeHardSkillsModel).where(
        EmployeeHardSkillsModel.employee_id == employee_id).all()
    return result

### Calculate employee weight

def get_employee_weight(employee_id: int, session: Session) -> float:
    return _calculate_employee_weight(employee_id=employee_id, session=session)

def _calculate_employee_weight(employee_id: int, session: Session):
    employee_hard_skills = get_user_hard_skills(employee_id=employee_id, session=session)
    employee_soft_skills = get_user_soft_skills(employee_id=employee_id, session=session)
    
    if len(employee_hard_skills) == 0 and len(employee_soft_skills) == 0:
        return 0
    
    logger.info('Employee Hard Skills: ', employee_hard_skills)
    logger.info('Employee Soft Skills: ', employee_soft_skills)
    
    soft_skills_ids = [skill.soft_skill_id for skill in employee_soft_skills]
    hard_skills_ids = [skill.hard_skill_id for skill in employee_hard_skills]
    
    soft_skills = get_soft_skills_by_ids(soft_skills_ids, session)
    hard_skills = get_hard_skills_by_ids(hard_skills_ids, session)
    
    logger.info('Soft Skills: ', soft_skills)
    logger.info('Hard Skills: ', hard_skills)
    
    weight = 0
    total_weight = 0
    for employee_skill, skill in zip(employee_hard_skills, hard_skills):
        weight += _calculate_skill_weight(skill.weight, employee_skill.domain)
        total_weight += skill.weight
    
    for employee_skill, skill in zip(employee_soft_skills, soft_skills):
        weight += _calculate_skill_weight(skill.weight, employee_skill.domain)
        total_weight += skill.weight
    return weight / total_weight if total_weight != 0 and weight != 0 else 0

def _calculate_skill_weight(weight: int, domain: int) -> int:
    return weight * domain

### Post employee Skills 

def post_user_soft_skills(
    employee_id: int, 
    soft_skill: EmployeeAbility,
    session: Session
) -> dict[str, any]:
    
    skills = get_user_soft_skills(employee_id=employee_id, session=session)
    
    soft_skill_db = EmployeeSoftSkillsModel()
    soft_skill_db.employee_id = employee_id
    soft_skill_db.domain = soft_skill.domain
    soft_skill_db.soft_skill_id = soft_skill.id
    
    session.add(soft_skill_db)
    session.commit()
    
    return {
        'response:': "Skills uploaded"
    }
    
def update_user_soft_skills(
    employee_id: int,
    skills_id: int,
    domain: int,
    session: Session):
        statement = session.query(EmployeeSoftSkillsModel).where(
            EmployeeSoftSkillsModel.employee_id == employee_id and
            EmployeeSoftSkillsModel.soft_skill_id == skills_id )
        result = session.execute(statement)
        skills_db = result.scalars().first()

        if skills_db:
            skills_db.id = id
            skills_db.name = skills_id
            skills_db.domain = domain

            session.commit()
            session.refresh(skills_db)
        else:
            raise HTTPException(status_code=404, detail=f"Soft Skill with id {id} not found")
        return skills_db
    
def delete_user_soft_skills(ids: List[int], session: Session):
    statement = session.query(EmployeeSoftSkillsModel).filter(EmployeeSoftSkillsModel.soft_skill_id.in_(ids))
    result = session.execute(statement)
    skills_db = result.scalars().all()
    session.delete_all(skills_db)
    session.commit()
    
### User hard skills

def post_user_hard_skills(
    employee_id: int, 
    hard_skill: EmployeeAbility,
    session: Session
) -> dict[str, any]:
    skills = get_user_hard_skills(employee_id=employee_id, session=session)
    
    hard_skill_db = EmployeeHardSkillsModel()
    hard_skill_db.employee_id = employee_id
    hard_skill_db.domain = hard_skill.domain
    hard_skill_db.hard_skill_id = hard_skill.id
    
    session.add(hard_skill_db)
    session.commit()
    
    return {
        'response:': "Skills uploaded"
    }
    
def update_user_hard_skills(
    employee_id: int,
    skills_id: int,
    domain: int,
    session: Session):
        statement = session.query(EmployeeHardSkillsModel).where(
            EmployeeHardSkillsModel.employee_id == employee_id and
            EmployeeHardSkillsModel.hard_skill_id == skills_id )
        result = session.execute(statement)
        skills_db = result.scalars().first()

        if skills_db:
            skills_db.id = id
            skills_db.name = skills_id
            skills_db.domain = domain

            session.commit()
            session.refresh(skills_db)
        else:
            raise HTTPException(status_code=404, detail=f"Hard Skill with id {id} not found")
        return skills_db
    
def delete_user_hard_skills(ids: List[int], session: Session):
    statement = session.query(EmployeeHardSkillsModel).filter(EmployeeHardSkillsModel.hard_skill_id.in_(ids))
    result = session.execute(statement)
    skills_db = result.scalars().all()
    session.delete_all(skills_db)
    session.commit()