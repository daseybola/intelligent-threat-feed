from random import random

def score_threats(data):
    for item in data:
        item["score"] = round(random(), 2)  # dummy ML scoring
    return data