from typing import List
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from requests import Session

from core.database.database import SessionLocal, get_session
import core.datasource.employee_datasource as ds
from entities.employee.employee import Employee, EmployeeUpdate
from entities.tables import *
from core.services.user_service import user_service

employee_router = APIRouter(prefix="/employees", tags=["employees"])
        
        
#Crud empleados
@employee_router.get(
    "/{id}", 
    status_code=status.HTTP_200_OK,
    # response_model=EmployeeModel
    )
def getEmployeeById(id: int, session: Session = Depends(get_session)):
    user = user_service.get_user()
    if user:
        return ds.getEmployee(id, session)
    else:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            content={"message": "Unauthorized Access"})

@employee_router.get(
    "/all",
    status_code=status.HTTP_200_OK,
    # response_model=List[Employee]
    )
def getEmployees(session: Session = Depends(get_session)):   
    try:
        user = user_service.get_user()
        if user:
            return ds.getAllEmployees(session)
        else:
            return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            content={"message": "Unauthorized Access"})
    except Exception as err:
        raise Exception(err)

@employee_router.put(
    "/{id}",
    status_code=status.HTTP_200_OK,
    )
def updateEmployee(id: int, 
                   employee: EmployeeUpdate, 
                   session: Session = Depends(get_session)):
    user = user_service.get_user()
    if user:
        return ds.updateEmployee(id, employee, session)
    else: 
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            content={"message": "Unauthorized Access"})

@employee_router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT
    )
def deleteEmployee(id: int, session: Session = Depends(get_session)):
    user = user_service.get_user()
    if user:
        return ds.deleteEmployee(id, session)
    else:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            content={"message": "Unauthorized Access"})

