from typing import List
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from requests import Session

import core.datasource.employee_datasource as ds
import entities.helpers.responses as resp

from core.database.database import SessionLocal, get_session
from entities.employee.employee import Employee, EmployeeUpdate
from entities.tables import *
from core.services.user_service import user_service


employee_router = APIRouter(prefix="/employees", tags=["employees"])
        
        
#Crud empleados
@employee_router.get(
    "/employee/{id}", 
    status_code=status.HTTP_200_OK,
    )
def getEmployeeById(id: int, session: Session = Depends(get_session)):
    user = user_service.get_user()
    
    try:
        if not user:
            return resp.not_logged_response
        if not user.is_admin:
            return resp.unauthorized_access_response
        return ds.getEmployee(id, session)
    except Exception as err:
        return resp.internal_server_error_response(err)

@employee_router.get(
    "/all",
    status_code=status.HTTP_200_OK,
    )
def getEmployees(session: Session = Depends(get_session)):   
    try:
        user = user_service.get_user()
        # if not user:
        #     return resp.not_logged_response
        # if not user.is_admin:
        #     return resp.unauthorized_access_response
        
        return ds.getAllEmployees(session)
        
    except Exception as err:
        return resp.internal_server_error_response(err)