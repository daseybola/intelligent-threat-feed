def normalize_feed_entry(entry):
    return {
        "value": entry["value"],
        "indicator_type": entry.get("type", "ip"),
        "source": entry.get("source", "unknown"),
        "normalized_data": {
            "value": entry["value"].strip(),
            "source": entry.get("source", "unknown")
        }
    }
