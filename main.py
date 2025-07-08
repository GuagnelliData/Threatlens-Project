# main.py
from src import config, preprocessing, model, evaluation

# 1. Load and preprocess dataset
print("📥 Loading and preprocessing data...")
data_path = config.TRAINING_SET_PATH  # CSV from CIC-IDS2017
X, y, label_encoder = preprocessing.load_and_prepare_data(data_path)
X_train_scaled, X_test_scaled, y_train, y_test = preprocessing.split_and_scale(X, y, config.RANDOM_STATE)
X_train_resampled, y_train_resampled = preprocessing.rebalance(X_train_scaled, y_train, config.RANDOM_STATE)

# 2. One-hot encode labels
num_classes = len(label_encoder.classes_)
y_train_cat, y_test_cat = model.one_hot_labels(y_train_resampled, y_test, num_classes)

# 3. Build and train the model
print("🧠 Building and training model...")
net = model.build_nn(input_dim=X_train_resampled.shape[1], output_dim=num_classes)
history = model.train(
    net,
    X_train_resampled, y_train_cat,
    X_test_scaled, y_test_cat,
    epochs=config.EPOCHS,
    batch_size=config.BATCH_SIZE
)

# 4. Evaluate
print("📊 Evaluating model performance...")
evaluation.report(net, X_test_scaled, y_test, label_encoder)
evaluation.plot_confusion_matrix(net, X_test_scaled, y_test, label_encoder, out_path="outputs/conf_matrix.png")

print("✅ Training completed!")
