from datetime import datetime, timedelta, timezone
import json
from fastapi import APIRouter
from fastapi import HTTPException
import uuid
# from jwt import encode
# import jwt


from core.services.user_service import user_service
from entities.auth.auth_data import *
from entities.tables.employee_tables import EmployeeModel 

auth_router = APIRouter(prefix="/auth", tags=["auth"])



# def verify_password(plain_password, hashed_password):
#     return pwd_context.verify(plain_password, hashed_password)


# def get_password_hash(password):
#     return pwd_context.hash(password)

def authenticate_user(email: str, password: str) -> EmployeeModel | None:
    user = user_service.get_user_by_email(email=email)
    if not user:
        return None
    if not password == user.password:
        return None
    return user

def create_access_token(user_data: dict, expires_delta: timedelta | None = None):
    payload = {}
    
    payload['user'] = user_data
    payload['exp'] = str(datetime.now(timezone.utc) + (
        expires_delta if expires_delta else timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    ))
    payload['jti'] = str(uuid.uuid4())
    
    # token = encode(payload=payload, key=SECRET_KEY, algorithm=ALGORITHM )
   
    return payload

async def get_current_active_user():
    current_user = user_service.get_user()
    if not current_user:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


