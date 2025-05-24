from fastapi import APIRouter
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app.models import ThreatIndicator
from app.config import DATABASE_URL

router = APIRouter()

@router.get("/threats")
def get_threats():
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        threats = session.query(ThreatIndicator).limit(100).all()
        return [dict(
            id=t.id,
            value=t.value,
            score=t.score,
            indicator_type=t.indicator_type
        ) for t in threats]
    finally:
        session.close()
