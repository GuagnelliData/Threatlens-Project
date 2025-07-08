import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report

def evaluate_model(model, X_test, y_test, label_encoder):
    y_pred = model.predict(X_test)
    y_pred_classes = np.argmax(y_pred, axis=1)

    cm = confusion_matrix(y_test, y_pred_classes)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=label_encoder.classes_)
    plt.figure(figsize=(10, 8))
    disp.plot(xticks_rotation=45, cmap='Blues')
    plt.title("ThreatLens1.2 — Confusion Matrix")
    plt.tight_layout()
    plt.savefig("confusion_matrix_threatlens12.png", dpi=300)
    plt.show()

    print("\n📋 Classification Report:")
    print(classification_report(y_test, y_pred_classes, target_names=label_encoder.classes_))

