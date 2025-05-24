import requests

def enrich_with_virustotal(ioc: str, api_key: str):
    headers = {"x-apikey": api_key}
    response = requests.get(f"https://www.virustotal.com/api/v3/urls/{ioc}", headers=headers)
    if response.status_code == 200:
        return response.json()
    return {}
