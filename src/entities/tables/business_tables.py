from sqlalchemy import Column, Integer, String
from core.database.database import Base


class DepartmentModel(Base):
    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(60), nullable=False)
    location = Column(String(60), nullable=False)
    
class PositionModel(Base):
    __tablename__ = 'positions'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(60), nullable=False)
