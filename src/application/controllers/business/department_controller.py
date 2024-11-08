from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from entities.business import Department
from core.database.database import get_session
from core.services.user_service import user_service
import core.datasource.business_datasource as bd
import entities.helpers.responses as resp

department_router = APIRouter(prefix="/business/departments", tags=["departments"])


@department_router.post(
    "/create",
    status_code=status.HTTP_201_CREATED
    )
def post_department(
    department: Department,
    session: Session = Depends(get_session)):
    user = user_service.get_user()
    
    try:
        # if user:
        return bd.create_department(department, session)
        # else:
        #     return resp.unauthorized_access_response
    except Exception as err:
        return resp.internal_server_error_response(err)
        
@department_router.get(
    "/all",
    status_code=status.HTTP_200_OK
)
def get_departments(
    session: Session = Depends(get_session)
):
    return bd.get_departments(session)

@department_router.put(
    "/update/{id}",
    status_code=status.HTTP_202_ACCEPTED
)
def update_department(  
    id: int,
    department: Department,
    session: Session = Depends(get_session)
    ):
    user = user_service.get_user()
    try:
        if not user:
            return resp.not_logged_response
        if not user.is_admin:
            return resp.unauthorized_access_response
        
        return bd.update_department(
            id=id, 
            department=department, 
            session=session)
        
    except Exception as err:
        return resp.internal_server_error_response(err) 
