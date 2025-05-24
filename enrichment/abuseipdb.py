import requests

def enrich_with_abuseipdb(ip: str, api_key: str):
    url = "https://api.abuseipdb.com/api/v2/check"
    headers = {"Key": api_key, "Accept": "application/json"}
    params = {"ipAddress": ip, "maxAgeInDays": 90}
    response = requests.get(url, headers=headers, params=params)
    return response.json() if response.ok else {}
