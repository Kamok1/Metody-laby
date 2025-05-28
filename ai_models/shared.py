import pandas as pd
from sklearn.model_selection import train_test_split

from data_process import process_data


def load_processed_data(path="../data/students.csv", sep=";", should_process=True):
    df = pd.read_csv(path, sep=sep)
    if should_process:
        df = process_data(df)
    return df

def load_train_with_validation_data(X, y, test_size=0.15, val_size=0.15, random_state=1):
    X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=(test_size + val_size), random_state=random_state)
    X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size= 1 - (val_size / (test_size + val_size)), random_state=random_state)
    return X_train, X_val, X_test, y_train, y_val, y_test
