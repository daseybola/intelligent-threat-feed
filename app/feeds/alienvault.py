import os

def fetch_otx():
    headers = {'X-OTX-API-KEY': os.getenv("OTX_API_KEY")}
    response = requests.get("https://otx.alienvault.com/api/v1/indicators/export?type=IPv4", headers=headers)
    if response.status_code == 200:
        lines = response.text.strip().split('\n')
        return [{"indicator": ip, "source": "OTX"} for ip in lines if ip and not ip.startswith("#")]
    return []