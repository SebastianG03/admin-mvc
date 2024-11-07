from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from entities.business import Position
from core.database.database import get_session
from core.services.user_service import user_service
import core.datasource.business_datasource as bd


position_router = APIRouter(prefix="/business/position", tags=["position"])

@position_router.post(
    "/create",
    status_code=status.HTTP_201_CREATED
)
def create_position(
    position: Position,
    session: Session = Depends(get_session)
):
    user = user_service.get_user()
    
    if user:
        return bd.create_position(position, session)
    else:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            content={"message": "Unauthorized Access"})
        
@position_router.get(
    "/all",
    status_code=status.HTTP_200_OK
)
def get_positions(session: Session = Depends(get_session)):
    return bd.get_positions(session)
        

@position_router.put(
    "/update/{id}",
    status_code=status.HTTP_202_ACCEPTED
)
def update_position(
    id: int,
    position: Position,
    session: Session = Depends(get_session)
):
    user = user_service.get_user()
    
    if user and user.is_admin:
        return bd.update_position(id, position, session)
    else:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            content={"message": "Unauthorized Access"})
        
@position_router.delete(
    "/delete/{id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_position(
    id: int,
    session: Session = Depends(get_session)
):
    user = user_service.get_user()
    
    if user and user.is_admin:
        return bd.delete_position(id)
    else:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            content={"message": "Unauthorized Access"})