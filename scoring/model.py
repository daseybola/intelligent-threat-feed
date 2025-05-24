# Run this standalone to generate the model
import pickle
from sklearn.ensemble import RandomForestClassifier

def train_dummy_model():
    X = [[0.1, 0.3], [0.9, 0.8], [0.5, 0.6]]
    y = [0, 1, 1]
    model = RandomForestClassifier()
    model.fit(X, y)
    with open("data/ml_model.pkl", "wb") as f:
        pickle.dump(model, f)

# Run once
if __name__ == "__main__":
    train_dummy_model()
