from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from entities.business import Department
from core.database.database import get_session
from core.services.user_service import user_service
import core.datasource.business_datasource as bd

department_router = APIRouter(prefix="/business/departments", tags=["departments"])


@department_router.post(
    "/create",
    status_code=status.HTTP_201_CREATED
    )
def post_department(
    department: Department,
    session: Session = Depends(get_session)):
    user = user_service.get_user()
    
    if user:
        return bd.create_department(department, session)
    else:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            content={"message": "Unauthorized Access"})
        
@department_router.get(
    "/all",
    status_code=status.HTTP_200_OK
)
def get_departments(
    session: Session = Depends(get_session)
):
    user = user_service.get_user()
    
    if user:
        return bd.get_departments(session)
    else:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            content={"message": "Unauthorized Access"})

@department_router.put(
    "/update/{id}",
    status_code=status.HTTP_202_ACCEPTED
)
def update_department(  
    id: int,
    department: Department,
    session: Session = Depends(get_departments)
    ):
    user = user_service.get_user()
    
    if user:
        return bd.update_department(
            id=id, 
            department=department, 
            session=session)
    else:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            content={"message": "Unauthorized Access"})
        
@department_router.delete(
    "/delete/{id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_department(
    id: int,
    session: Session = Depends(get_session)
    ):
    user = user_service.get_user()
    
    if user: 
        return bd.delete_department(id, session)
    else:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            content={"message": "Unauthorized Access"})