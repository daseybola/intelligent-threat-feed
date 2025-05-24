import requests

def fetch_urlhaus():
    response = requests.get("https://urlhaus.abuse.ch/downloads/csv_recent/")
    indicators = []
    if response.status_code == 200:
        for line in response.text.splitlines():
            if line.startswith("http"):
                indicators.append({"indicator": line.split(",")[2], "source": "URLHaus"})
    return indicators