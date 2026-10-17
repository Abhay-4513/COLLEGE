# Compare Sigmoid, ReLU, Tanh, and Leaky ReLU using TensorFlow/Keras
# Dataset: Breast Cancer Wisconsin (binary classification)
# Install: pip install tensorflow scikit-learn pandas numpy matplotlib

import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# 1. Load binary classification dataset
X, y = load_breast_cancer(return_X_y=True)

# Keep the test data separate from the training/validation data
X_train_all, X_test, y_train_all, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)
X_train, X_val, y_train, y_val = train_test_split(
    X_train_all, y_train_all, test_size=0.20,
    random_state=42, stratify=y_train_all
)

# Scale features using only the training subset
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train).astype("float32")
X_val = scaler.transform(X_val).astype("float32")
X_test = scaler.transform(X_test).astype("float32")
y_train = y_train.astype("float32")
y_val = y_val.astype("float32")
y_test = y_test.astype("float32")

# 2. Define the activation functions in one place
ACTIVATIONS = ["sigmoid", "relu", "tanh", "leaky_relu"]


def make_activation(name):
    """Return the requested Keras activation layer."""
    if name == "leaky_relu":
        return tf.keras.layers.LeakyReLU(negative_slope=0.01)
    return tf.keras.layers.Activation(name)


def build_model(activation_name, input_features):
    """Build the same multi-hidden-layer architecture for each activation."""
    model = tf.keras.Sequential([
        tf.keras.layers.Input(shape=(input_features,)),
        tf.keras.layers.Dense(64), make_activation(activation_name),
        tf.keras.layers.Dense(32), make_activation(activation_name),
        tf.keras.layers.Dense(16), make_activation(activation_name),
        tf.keras.layers.Dense(1, activation="sigmoid")
    ])
    model.compile(
        optimizer="adam",
        loss="binary_crossentropy",
        metrics=["accuracy"]
    )
    return model


# 3. Train and evaluate each activation function
results = []

for activation_name in ACTIVATIONS:
    # Reset seeds so the experiments are more reproducible
    tf.keras.backend.clear_session()
    tf.keras.utils.set_random_seed(42)

    model = build_model(activation_name, X_train.shape[1])
    early_stopping = tf.keras.callbacks.EarlyStopping(
        monitor="val_loss",
        patience=10,
        restore_best_weights=True
    )

    start_time = time.perf_counter()
    history = model.fit(
        X_train, y_train,
        validation_data=(X_val, y_val),
        epochs=100,
        batch_size=32,
        callbacks=[early_stopping],
        verbose=0
    )
    training_time = time.perf_counter() - start_time

    # Epoch with the lowest validation loss is used as convergence measure
    best_epoch = int(np.argmin(history.history["val_loss"]) + 1)
    test_loss, test_accuracy = model.evaluate(X_test, y_test, verbose=0)

    results.append({
        "Activation": activation_name.replace("_", " ").title(),
        "Test Accuracy (%)": test_accuracy * 100,
        "Best Epoch": best_epoch,
        "Training Time (s)": training_time,
        "Test Loss": test_loss
    })

# 4. Display comparison table
results_df = pd.DataFrame(results).sort_values(
    by="Test Accuracy (%)", ascending=False
)
print("\nActivation Function Performance Comparison")
print(results_df.to_string(index=False, formatters={
    "Test Accuracy (%)": "{:.2f}".format,
    "Training Time (s)": "{:.2f}".format,
    "Test Loss": "{:.4f}".format
}))

# 5. Plot bar charts for test accuracy and convergence speed
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Accuracy: higher is better
axes[0].bar(results_df["Activation"], results_df["Test Accuracy (%)"])
axes[0].set_title("Test Accuracy by Activation Function")
axes[0].set_ylabel("Test Accuracy (%)")
axes[0].set_ylim(0, 100)
axes[0].tick_params(axis="x", rotation=20)
for i, value in enumerate(results_df["Test Accuracy (%)"]):
    axes[0].text(i, value + 0.5, f"{value:.2f}%", ha="center", fontsize=9)

# Best epoch: fewer epochs generally means faster convergence
convergence_df = results_df.sort_values("Activation")
axes[1].bar(convergence_df["Activation"], convergence_df["Best Epoch"])
axes[1].set_title("Convergence Speed (Best Validation Epoch)")
axes[1].set_ylabel("Epoch")
axes[1].tick_params(axis="x", rotation=20)
for i, value in enumerate(convergence_df["Best Epoch"]):
    axes[1].text(i, value + 0.5, str(value), ha="center", fontsize=9)

plt.tight_layout()
plt.show()
