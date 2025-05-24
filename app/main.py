from feeds.alienvault import fetch_otx
from feeds.urlhaus import fetch_urlhaus
from feeds.virustotal import fetch_virustotal
from feeds.abuseipdb import fetch_abuseipdb
from enrich.enrich import enrich_data
from ml.scorer import score_threats
from db.models import init_db, save_to_db

print("Starting pipeline...")

feeds = []
feeds += fetch_otx()
feeds += fetch_urlhaus()
feeds += fetch_virustotal()
feeds += fetch_abuseipdb()

print(f"Fetched {len(feeds)} indicators")

enriched = enrich_data(feeds)
scored = score_threats(enriched)

init_db()
save_to_db(scored)

print("Pipeline complete. Data stored in PostgreSQL.")