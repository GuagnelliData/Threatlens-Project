# 🛡️ ThreatLens — UNSW-NB15 Analysis & Classification Toolkit  
**Author:** Carlos Joseph Guagnelli  
**Start Date:** 2025-06-24  
**Status:** 🚧 Actively Developed

---

## 📘 Project Overview  
**ThreatLens** is a modular toolkit for analyzing, preprocessing, and classifying the UNSW-NB15 dataset. It is designed to support training and evaluation of intrusion detection systems (IDS) using machine learning and neural networks.

The project offers a complete pipeline — from raw data ingestion to multiclass attack classification — using Python, data visualization, and deep learning.

---

## 🧠 Motivation  
In an increasingly connected world, cybersecurity threats demand automated and adaptive detection systems. **ThreatLens** was born out of the need to train intelligent models capable of recognizing malicious patterns within large volumes of network traffic.

It brings together data science, visualization, and deep learning in a modular, scalable structure.

---

## 📂 Dataset  
- **Name:** UNSW-NB15 (training-set only)  
- **Source:** Australian Centre for Cyber Security  
- **Records:** ~175,341  
- **Features:** 45 (numerical and categorical)  
- **Labels:**  
  - `label`: 0 = normal traffic, 1 = attack  
  - `attack_cat`: attack category (10 classes)

---

## ✅ Current Progress

- ✅ Dataset exploration with `pandas`
- ✅ Distribution analysis of normal vs. attack traffic (`label`)
- ✅ Attack category breakdown (`attack_cat`)
- ✅ Label encoding (`attack_cat`) with `LabelEncoder`
- ✅ One-hot encoding of categorical variables (`proto`, `service`, `state`)
- ✅ Dataset splitting (80/20, stratified)
- ✅ Feature scaling with `StandardScaler`
- ✅ Class rebalance with **SMOTE** (via `imbalanced-learn`)
- ✅ Multiclass neural network training with TensorFlow + Keras
- ✅ >99% validation accuracy
- ✅ Confusion matrix visualization
- ✅ Modular code structure (`src/`) and configuration file

---

## 🛠️ Technologies Used

- **Language:** Python 3.11  
- **Virtual Environment:** `venv`  
- **Key Libraries:**  
  - `pandas`, `numpy` → data manipulation  
  - `matplotlib`, `seaborn` → visualization  
  - `scikit-learn` → preprocessing, encoding, metrics  
  - `imbalanced-learn` → class balancing (SMOTE)  
  - `tensorflow`, `keras` → deep learning

---

## 📊 Initial Results

Basic MLP model:
```python
[Input] → Dense(128, ReLU) → Dropout(0.3) → Dense(64, ReLU) → Dropout(0.3) → Output(Softmax)

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar el script principal
python Threatlens1.py
