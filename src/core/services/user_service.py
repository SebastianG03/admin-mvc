import base64
from datetime import datetime, timezone
from jwt import decode
from sqlalchemy import select
from entities.tables.employee_tables import EmployeeModel
from entities.auth.user import User 
from entities.tables.business_tables import PositionModel      
from entities.auth.auth_data import ADMIN_ROLES, ALGORITHM, SECRET_KEY
from core.services.logger_service import logger

from core.database.database import SessionLocal


class UserService:
    def __init__(self):
        self.session = SessionLocal()
        self.user: User | None = None
    
    def get_user_by_email(self, email: str) -> EmployeeModel | None:
        statement = select(EmployeeModel).where(EmployeeModel.email == email)
        result = self.session.execute(statement)
        return result.scalars().first()
    
    def get_position_by_id(self, position_id: int) -> PositionModel | None:
        return self.session.get(PositionModel, position_id)
        # statement = self.session.scalars(select(PositionModel).where(PositionModel.id == position_id))
        # result = self.session.execute(statement)
        # return result.scalars().first()
        
        
    def set_user(self, user: User):
        position: PositionModel = self.get_position_by_id(user.user_data.position_id)
        name: str = position.name.lower()
        
        is_admin = [x for x in ADMIN_ROLES if x in name]
        user.is_admin = len(is_admin) > 0
        self.user = user
        
    
        
    def logout(self):
        self.user = None
    
    def get_user(self) -> User | None : 
        is_expire = self.toke_is_expire()
        
        if is_expire:
            self.logout()
            return None
        else:
            return self.user
            
    
    def user_json(self) -> dict:
        if self.user is None:
            return {}
        data: EmployeeModel = self.user.user_data
        dict_data = data.to_dict()
        token = self.user.token.model_dump()
        # dict_data['token'] = token
        return dict_data
    
    def toke_is_expire(self) -> bool:
        user = self.user
        if user is None:
            return True
        token = user.token.access_token
        payload = decode(token, key=SECRET_KEY, algorithms=[ALGORITHM])
        exp = payload['exp']
        iat = payload['iat']
        create_time = datetime.fromtimestamp(iat)
        expire_time = datetime.fromtimestamp(exp)
        # logger.info('create_time: ' + str(create_time) + ' expire_time: ' + str(expire_time))
        if create_time > expire_time:
            return True
        return False

    
user_service = UserService()
