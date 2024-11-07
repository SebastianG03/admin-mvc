from sqlalchemy import Column, Integer, ForeignKey
from core.database.database import Base

class EmployeeSoftSkillsModel(Base):
    __tablename__ = 'employee_soft_skills'

    employee_id = Column(Integer, ForeignKey('employees.id'), primary_key=True)
    soft_skill_id = Column(Integer, ForeignKey('soft_skills.id'))
    domain = Column(Integer, nullable=False)
    
    def to_dict(self):
        return {
            'employee_id': self.employee_id,
            'soft_skill_id': self.soft_skill_id,
            'domain': self.domain
        }
    
class EmployeeHardSkillsModel(Base):
    __tablename__ = 'employee_hard_skills'

    employee_id = Column(Integer, ForeignKey('employees.id'), primary_key=True)
    hard_skill_id = Column(Integer, ForeignKey('hard_skills.id'))
    domain = Column(Integer, nullable=False)
    
    def to_dict(self):
        return {
            'employee_id': self.employee_id,
            'hard_skill_id': self.hard_skill_id,
            'domain': self.domain
        }
    
