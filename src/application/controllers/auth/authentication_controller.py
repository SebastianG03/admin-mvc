import json
from fastapi import APIRouter, Response, status


from fastapi import Depends
from fastapi.responses import JSONResponse
from requests import Session


import core.datasource.employee_datasource as ds
from core.datasource.auth_datasource import (
    authenticate_user)
from entities.employee.employee import Employee, EmployeeUpdate
from entities.auth.token import Token
from entities.auth.user import LoginModel, User
from core.services.user_service import user_service
from core.database.database import get_session
from entities.employee.workload import Workload
from entities.tables.employee_tables import EmployeeModel

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.post("/token")
def login_for_access_token(
    login_data: LoginModel) -> Token:
    user = authenticate_user(login_data.email, login_data.password)
    if not user:
        return Response(status_code=400, content="Incorrect email or password")
    
    user_service.set_user(user = User(user_data = user))
    
    return Response(content="Login successful") 


@auth_router.get("/users/me/")
async def read_users_me():
    user = user_service.get_user()
    if user:
        data: EmployeeModel = user.user_data
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=user_service.user_json(),
        )
    else:
        return Response("Not logged in")

@auth_router.post(
    "/users/create",
    status_code=status.HTTP_201_CREATED,
    )
def create_user(employee: Employee, session: Session = Depends(get_session)):
    user = user_service.get_user()
    validation = user_service.get_user_by_email(email=employee.email)
    if validation:
        return Response(content="User already exists. Log in instead.")
    
    if not user:
        try:
            ds.createEmployee(employee, session)
        except Exception as err:
            return Response(content=err, status_code=status.HTTP_400_BAD_REQUEST)
        user = user_service.get_user_by_email(email=employee.email)
        user_service.set_user(user = User(user_data=user))     
        return Response(content="User created and logged.")
    else:
        return Response(content="You are already logged. Log out before create an account")

@auth_router.put(
    "/users/update/{id}",
    status_code=status.HTTP_200_OK,
    )
def updateEmployee(employee: EmployeeUpdate, 
                   session: Session = Depends(get_session)):
    user: User = user_service.get_user()
    if user:
        return ds.updateEmployee(user.user_data.id, employee, session)
    else: 
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            content={"message": "Unauthorized Access"})


@auth_router.get(
    "/users/logout",
    status_code=status.HTTP_200_OK,
)
def logout():
    user = user_service.get_user()
    if user:
        user_service.logout()
        return Response("Logout successfully")
        
    return Response("You are not logged. Log in first")
    
