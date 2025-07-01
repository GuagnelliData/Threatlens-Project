# src/preprocessing.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

def load_and_preprocess_data():
    df = pd.read_csv("data/UNSW_NB15_training-set.csv")
    
    le = LabelEncoder()
    df['attack_cat_encoded'] = le.fit_transform(df['attack_cat'])

    X = df.drop(columns=['id', 'label', 'attack_cat'])
    X = pd.get_dummies(X, columns=['proto', 'service', 'state'], drop_first=True)
    y = df['attack_cat_encoded']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=42
    )

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, X_test_scaled, y_train, y_test
