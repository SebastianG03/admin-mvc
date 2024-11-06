from fastapi import APIRouter, Response, status
from datetime import  timedelta
from typing import Annotated

from fastapi import Depends


import core.datasource.employee_datasource as ds
from core.database.database import SessionLocal
from core.datasource.auth_datasource import (
    ACCESS_TOKEN_EXPIRE_MINUTES, 
    authenticate_user,
    create_access_token, 
    get_current_active_user)
from entities.employee.employee import Employee
from entities.auth.token import Token
from entities.auth.user import LoginModel, User
from core.services.user_service import user_service


auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.post("/token")
def login_for_access_token(
    login_data: LoginModel) -> Token:
    user = authenticate_user(login_data.email, login_data.password)
    if not user:
        return Response(status_code=400, content="Incorrect email or password")
    # access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    # access_token = create_access_token(
    #     user_data={
    #         "email": user.email,
    #         "user_id": user.id,
    #         "role": "employee"
    #         },
    #     expires_delta=access_token_expires,
    # )
    # token = Token(access_token=access_token, token_type="bearer")
    user_service.set_user(user = User(user_data=user))
    
    return Response(content="Login successful") 


@auth_router.get("/users/me/")
async def read_users_me():
    user = user_service.get_user()
    if user:
        return user
    else:
        return Response("Not logged in")

@auth_router.post(
    "/users/create",
    status_code=status.HTTP_201_CREATED,
    )
def createEmployee(employee: Employee):
    session = SessionLocal()
    user = user_service.get_user()
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
    
