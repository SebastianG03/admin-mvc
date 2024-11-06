from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from core.database.database import Base


class EmployeeModel(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True, autoincrement=True)
    password = Column(String(265), nullable=False)
    name = Column(String(60), nullable=False)
    department_id = Column(Integer, ForeignKey('departments.id'), nullable=False)  # Asume que hay una tabla 'departments'
    position_id = Column(Integer, ForeignKey('positions.id'), nullable=False)
    workload = Column(Integer, nullable=False)
    salary = Column(Float, nullable=False)
    email = Column(String(120), nullable=False)
    phone = Column(String(20), nullable=True)
    address = Column(String(120), nullable=True)
    soft_skills = relationship("SoftSkillsModel", secondary="employee_soft_skills")
    hard_skills = relationship("HardSkillsModel", secondary="employee_hard_skills")