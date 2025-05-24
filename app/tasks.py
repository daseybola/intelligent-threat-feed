import requests
from app.utils.normalization import normalize_feed_entry
from app.utils.enrichment import enrich_indicator
from app.utils.scoring import score_indicator
from app.models import ThreatIndicator
from app.config import DATABASE_URL, REDIS_URL
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import redis

cache = redis.Redis.from_url(REDIS_URL)
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def fetch_open_threat_feed():
    return [
        {"value": "8.8.8.8", "type": "ip", "source": "openfeed1"},
        {"value": "1.1.1.1", "type": "ip", "source": "openfeed2"},
    ]

def is_duplicate(val):
    if cache.sismember("processed_indicators", val):
        return True
    cache.sadd("processed_indicators", val)
    return False

def save_to_db(data):
    session = Session()
    try:
        record = ThreatIndicator(**data)
        session.add(record)
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"DB error: {e}")
    finally:
        session.close()

def ingest_and_process():
    feed = fetch_open_threat_feed()
    for entry in feed:
        norm = normalize_feed_entry(entry)
        if is_duplicate(norm["value"]):
            continue
        enriched = enrich_indicator(norm)
        enriched["score"] = score_indicator(enriched)
        save_to_db(enriched)
