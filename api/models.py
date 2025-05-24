from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .database import Base

class IOC(Base):
    __tablename__ = "iocs"
    id = Column(Integer, primary_key=True, index=True)
    indicator = Column(String, unique=True, index=True)
    score = Column(Integer)
    source = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
