from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from entities.business import Position
from core.database.database import get_session
from core.services.user_service import user_service
import core.datasource.business_datasource as bd
import entities.helpers.responses as resp


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
    
    try:
        # if user:
        return bd.create_position(position, session)
        # else:
        #     return resp.unauthorized_access_response
    except Exception as err:
        return resp.internal_server_error_response(err)
        
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
    
    try:
        if not user:
            return resp.not_logged_response
        if not user.is_admin:
            return resp.unauthorized_access_response
        return bd.update_position(id, position, session)
    except Exception as err:
        return resp.internal_server_error_response(err)