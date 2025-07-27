import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from preprocessing import load_and_preprocess

# Load and merge all signal types
X_total, y_total = [], []

for signal in ["rssi", "csi", "tof"]:
    X, y = load_and_preprocess(signal)
    X_total.extend(X)
    y_total.extend(y)

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_total, y_total)

# Evaluate
preds = model.predict(X_total)
print("✅ Training Accuracy:", accuracy_score(y_total, preds))
print("\n🔍 Classification Report:\n", classification_report(y_total, preds))

# Save model
joblib.dump(model, "iot_security_system/models/iot_rf_model.pkl")
print("✅ Model saved to: iot_security_system/models/iot_rf_model.pkl")
