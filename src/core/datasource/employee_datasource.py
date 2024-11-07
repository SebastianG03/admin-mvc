from typing import List
from fastapi import HTTPException
from sqlalchemy.orm import Session

from entities.employee.employee import Employee, EmployeeUpdate
from entities.tables import *
from core.services.user_service import user_service

def getEmployee(
    id: int,
    session: Session) -> EmployeeModel:
    employee = session.query(EmployeeModel).get(id) 

    if not employee:
        raise HTTPException(status_code=404, detail=f"Employee with id {id} not found")
    return employee

def getAllEmployees(session: Session) -> List[EmployeeModel]: 
    task_list = session.query(EmployeeModel).all() 
    return task_list

def createEmployee(
        employee: Employee,
        session: Session) -> dict[str, any]:
    try:
        result = user_service.get_user_by_email(employee.email)
        if result:
            raise HTTPException(status_code=400, detail=f"Employee with email {employee.email} already exists")
        employee_data = employee.model_dump()
        employee_db = EmployeeModel(**employee_data)

        session.add(employee_db)
        session.commit()
        session.refresh(employee_db)

        return employee_data
    except Exception as err:
        raise err

def updateEmployee(
    id: int, 
    employee: EmployeeUpdate, 
    session: Session) -> dict[str, any]:
    employee_db = session.query(EmployeeModel).get(id)  # Get given id

    if employee_db:
        employee.id = id
        employee_data = employee.model_dump()

        employee_db = EmployeeModel(**employee_data)
        
        for key, value in employee_data.items():
            setattr(employee_db, key, value)
    
        employee_db = employee_data
        session.commit()
        session.refresh(employee_db)
    else:
        raise HTTPException(status_code=404, detail=f"Employee with id {id} not found")

    return employee_db

def deleteEmployee(id: int, session: Session):
    employee_db = session.query(EmployeeModel).get(id)
    if employee_db:
        session.delete(employee_db)
        session.commit()
    else:
        raise HTTPException(status_code=404, detail=f"Employee with id {id} not found")
    return None

