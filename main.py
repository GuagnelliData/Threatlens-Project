# main.py

from src.preprocessing import load_and_preprocess_data
from src.model_nn import train_neural_network

print("🚀 ThreatLens inicializando...")

X_train_scaled, X_test_scaled, y_train, y_test = load_and_preprocess_data()
model = train_neural_network(X_train_scaled, y_train, X_test_scaled, y_test)

print("✅ Entrenamiento completo.")
