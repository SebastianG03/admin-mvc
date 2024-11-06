from sqlalchemy import Sequence, select
from core.database.database import SessionLocal
from entities.tables.employee_tables import EmployeeModel
from entities.auth.user import User        


class UserService:
    def __init__(self):
        self.session = SessionLocal()
        self.user: User | None = None
    
    def get_user_by_email(self, email) -> EmployeeModel | None:
        # with self.session as session:
        statement = select(EmployeeModel).where(EmployeeModel.email == email)
        result = self.session.execute(statement)
        return result.scalars().first()
        
    def set_user(self, user: User):
        self.user = user
        
    def logout(self):
        self.user = None
    
    def get_user(self) -> User | None : 
        
        return self.user
    
user_service = UserService()
