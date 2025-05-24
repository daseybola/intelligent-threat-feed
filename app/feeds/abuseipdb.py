import requests
import os

def fetch_abuseipdb():
    headers = {'Key': os.getenv("ABUSEIPDB_KEY")}
    indicators = []
    sample_ips = ["8.8.8.8", "1.1.1.1"]
    for ip in sample_ips:
        url = f"https://api.abuseipdb.com/api/v2/check?ipAddress={ip}&maxAgeInDays=90"
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            indicators.append({"indicator": ip, "source": "AbuseIPDB"})
    return indicators