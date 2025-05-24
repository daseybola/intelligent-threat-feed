import pickle
import os

model = pickle.load(open("data/ml_model.pkl", "rb"))

def score_ioc(enriched_data: dict):
    # Example feature extraction (dummy)
    vt_score = enriched_data.get("vt_score", 0)
    abuse_score = enriched_data.get("abuse_score", 0)
    score = model.predict([[vt_score, abuse_score]])[0]
    return int(score)
