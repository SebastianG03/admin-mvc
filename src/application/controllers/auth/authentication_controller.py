from fastapi import APIRouter, Response, status


from fastapi import Depends
from fastapi.responses import JSONResponse
from requests import Session


import core.datasource.employee_datasource as ds
import entities.helpers.responses as resp
from core.datasource.auth_datasource import (
    authenticate_user)
from entities.employee.employee import Employee, EmployeeUpdate
from entities.auth.token import Token
from entities.auth.user import LoginModel, User
from core.services.user_service import user_service
from core.database.database import get_session
from entities.tables.employee_tables import EmployeeModel

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.post("/token")
def login_for_access_token(
    login_data: LoginModel) -> Token:
    try:
        user = authenticate_user(login_data.email, login_data.password)
        if not user:
            return resp.invalid_tokens_response
    
        user_service.set_user(user = User(user_data = user))
        return resp.login_successful_response 
    except Exception as err:
        return resp.internal_server_error_response(err)

@auth_router.get("/users/me/")
async def read_users_me():
    user = user_service.get_user()
    try:
        if user:
            data: EmployeeModel = user.user_data
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content=user_service.user_json(),
            )
        else:
            return resp.not_logged_response
    except Exception as err:
        return resp.internal_server_error_response(err)
    
@auth_router.post(
    "/users/create",
    status_code=status.HTTP_201_CREATED,
    )
def create_user(employee: Employee, session: Session = Depends(get_session)):
    try:
        user = user_service.get_user()
        if user:
            return resp.already_logged_response
        
        validation = user_service.get_user_by_email(email=employee.email)
        if validation:
            return resp.user_exists_response

        ds.createEmployee(employee, session)
        user = user_service.get_user_by_email(email=employee.email)
        user_service.set_user(user = User(user_data=user))     
        return Response(content="User created and logged.")
    except Exception as err:
        return resp.internal_server_error_response(err)
    
@auth_router.put(
    "/users/update/{id}",
    status_code=status.HTTP_200_OK,
    )
def updateEmployee(employee: EmployeeUpdate, 
                   session: Session = Depends(get_session)):
    user: User = user_service.get_user()
    try:
        if user:
            return ds.updateEmployee(user.user_data.id, employee, session)
        else: 
            return resp.not_logged_response
    except Exception as err:
        return resp.internal_server_error_response(err)


@auth_router.get(
    "/users/logout",
    status_code=status.HTTP_200_OK,
)
def logout():
    user = user_service.get_user()
    
    try:
        if user:
            user_service.logout()
            resp.logout_response(True)

        return resp.logout_response(False)
    except Exception as err:
        return resp.internal_server_error_response(err)