def enrich_data(data):
    for entry in data:
        entry["geo"] = "N/A"  # placeholder for actual enrichment logic
        entry["asn"] = "N/A"
    return data