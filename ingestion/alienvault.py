import requests

def fetch_alienvault_iocs(api_key: str):
    url = "https://otx.alienvault.com/api/v1/pulses/subscribed"
    headers = {"X-OTX-API-KEY": api_key}
    response = requests.get(url, headers=headers)
    iocs = []
    if response.ok:
        for pulse in response.json().get("results", []):
            iocs.extend([ioc["indicator"] for ioc in pulse["indicators"]])
    return iocs
