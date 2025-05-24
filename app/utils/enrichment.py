def enrich_indicator(indicator):
    return {
        **indicator,
        "enrichment_data": {
            "geo": "US",
            "asn": "AS15169",
            "category": "Public DNS"
        }
    }
