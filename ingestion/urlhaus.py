import requests

def fetch_urlhaus_iocs():
    url = "https://urlhaus.abuse.ch/downloads/csv_recent/"
    response = requests.get(url)
    iocs = []
    if response.ok:
        lines = response.text.splitlines()
        for line in lines[9:]:  # skip headers
            parts = line.split(',')
            if parts and parts[2]:
                iocs.append(parts[2].strip())
    return iocs
