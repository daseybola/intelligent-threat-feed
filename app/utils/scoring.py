def score_indicator(indicator):
    if "dns" in indicator["enrichment_data"].get("category", "").lower():
        return 90
    return 50
