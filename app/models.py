from sqlalchemy import Column, Integer, String, JSON, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class ThreatIndicator(Base):
    __tablename__ = "indicators"
    id = Column(Integer, primary_key=True)
    value = Column(String)
    indicator_type = Column(String)
    source = Column(String)
    normalized_data = Column(JSON)
    enrichment_data = Column(JSON)
    score = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)
