from fastapi import FastAPI
from ingestion.alienvault import fetch_alienvault_iocs
from ingestion.urlhaus import fetch_urlhaus_iocs
from enrichment.virustotal import enrich_with_virustotal
from enrichment.abuseipdb import enrich_with_abuseipdb
from scoring.scorer import score_ioc
from .models import IOC
from .database import SessionLocal, engine, Base
import os

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/ingest/")
def ingest():
    db = SessionLocal()
    iocs = set(fetch_alienvault_iocs(os.getenv("ALIENVAULT_API_KEY")) + fetch_urlhaus_iocs())
    for ioc in iocs:
        vt = enrich_with_virustotal(ioc, os.getenv("VT_API_KEY"))
        abuse = enrich_with_abuseipdb(ioc, os.getenv("ABUSEIPDB_API_KEY"))
        enriched = {
            "vt_score": vt.get("data", {}).get("attributes", {}).get("last_analysis_stats", {}).get("malicious", 0),
            "abuse_score": abuse.get("data", {}).get("abuseConfidenceScore", 0),
        }
        score = score_ioc(enriched)
        db_ioc = IOC(indicator=ioc, score=score, source="auto")
        try:
            db.add(db_ioc)
            db.commit()
        except:
            db.rollback()
    db.close()
    return {"status": "success", "count": len(iocs)}
