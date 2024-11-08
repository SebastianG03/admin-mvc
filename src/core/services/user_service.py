from sqlalchemy import Sequence, select
from core.database.database import SessionLocal
from entities.tables.employee_tables import EmployeeModel
from entities.auth.user import User 
from entities.tables.business_tables import PositionModel      
from entities.auth.auth_data import ADMIN_ROLES 


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
        return self.user
    
    def user_json(self) -> dict:
        if self.user is None:
            return {}
        data: EmployeeModel = self.user.user_data
        return data.to_dict()
    
user_service = UserService()
