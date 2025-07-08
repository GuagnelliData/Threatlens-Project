import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from imblearn.over_sampling import SMOTE

def encode_labels(df):
    le = LabelEncoder()
    df['Label_Encoded'] = le.fit_transform(df['Label'])
    return df, le

def prepare_features(df):
    X = df.select_dtypes(include=[np.number]).drop(columns=['Label_Encoded'], errors='ignore')
    y = df['Label_Encoded']
    return X, y

def split_and_scale(X, y, test_size, random_state):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, stratify=y, random_state=random_state)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    return X_train_scaled, X_test_scaled, y_train, y_test

def rebalance_data(X, y, random_state):
    smote = SMOTE(random_state=random_state)
    X_res, y_res = smote.fit_resample(X, y)
    return X_res, y_res
