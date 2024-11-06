from fastapi import HTTPException
from sqlalchemy import Sequence
from sqlalchemy.orm import Session

from entities.tables.skills_tables import HardSkillsModel, SoftSkillsModel
from entities.tables.employee_skills_tables import EmployeeHardSkillsModel, EmployeeSoftSkillsModel
from entities.employee.hard_skills import HardSkills
from entities.employee.soft_skills import SoftSkills

### User Skills table

def get_user_soft_skills(
    employee_id: int, 
    session: Session) -> Sequence[EmployeeSoftSkillsModel]:
    statement = session.query(EmployeeSoftSkillsModel).where(
        EmployeeSoftSkillsModel.employee_id == employee_id)
    result = session.execute(statement)
    return result.scalars().all()

def get_user_hard_skills(
    employee_id: int, 
    session: Session) -> Sequence[EmployeeHardSkillsModel]:
    statement = session.query(EmployeeHardSkillsModel).where(
        EmployeeHardSkillsModel.employee_id == employee_id)
    result = session.execute(statement)
    return result.scalars().all()

### Post employee Skills 

def post_user_soft_skills(
    employee_id: int, 
    soft_skill_id: int,
    domain: int,
    session: Session
) -> dict[str, any]:
    soft_skill_db = EmployeeSoftSkillsModel()
    soft_skill_db.soft_skill_id = soft_skill_id
    soft_skill_db.employee_id = employee_id
    soft_skill_db.domain = domain
    
    session.add(soft_skill_db)
    session.commit()
    session.refresh(soft_skill_db)
    
    return {
        'employee_id:': employee_id,
        'soft_skill_id:': soft_skill_id,
        'domain:': domain 
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

def post_user_hard_skills(
    employee_id: int, 
    hard_skill_id: int,
    domain: int,
    session: Session
) -> dict[str, any]:
    hard_skill_db = EmployeeHardSkillsModel()
    hard_skill_db.hard_skill_id = hard_skill_id
    hard_skill_db.employee_id = employee_id
    hard_skill_db.domain = domain
    
    session.add(hard_skill_db)
    session.commit()
    session.refresh(hard_skill_db)
    
    return {
        'employee_id:': employee_id,
        'hard_skill_id:': hard_skill_id,
        'domain:': domain 
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