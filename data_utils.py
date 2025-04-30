import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import spacy

# Load a small English NLP model
nlp = spacy.load("en_core_web_sm")

def load_dataset():
    """Loads the dataset used throughout the app."""
    return pd.read_csv("data/cleaned_climate_data.csv")

def preprocess_features(data, test_ratio=0.2):
    X = data.drop(columns=["avg_max_temp", "year"])
    y = data["avg_max_temp"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_ratio, random_state=42)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    return X_train_scaled, X_test_scaled, y_train, y_test, scaler

def save_trained_model(model, name):
    joblib.dump(model, f"models/{name}.pkl")

def load_trained_model(name):
    return joblib.load(f"models/{name}.pkl")

def analyze_input_text(text):
    doc = nlp(text)
    return {
        "tokens": [token.text for token in doc],
        "pos_tags": [token.pos_ for token in doc],
        "lemmas": [token.lemma_ for token in doc],
        "entities": [(ent.text, ent.label_) for ent in doc.ents]
    }
