from sqlalchemy import Column, Integer, String
from database import Base

class AutoPart(Base):
    __tablename__ = 'autoparts'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)

