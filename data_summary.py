import os

import pandas as pd


def get_numeric_statistics(df, numeric_categories = None):
    stats = pd.DataFrame()

    if numeric_categories is not None:
        numeric_features = numeric_categories
    else:
        numeric_features = df.select_dtypes(include='number').columns

    stats['Mean'] = df[numeric_features].mean()
    stats['Median'] = df[numeric_features].median()
    stats['Min'] = df[numeric_features].min()
    stats['Max'] = df[numeric_features].max()
    stats['Std'] = df[numeric_features].std()
    stats['5th Percentile'] = df[numeric_features].quantile(0.05)
    stats['95th Percentile'] = df[numeric_features].quantile(0.95)
    stats['Missing Values'] = df[numeric_features].isnull().sum()
    stats['Unique'] = df[numeric_features].nunique()

    return stats


def get_categorical_statistics(df, categorical_categories = None):
    cat_stats = []

    if categorical_categories is not None:
        cat_features = categorical_categories
    else:
        cat_features = df.select_dtypes(include='object').columns

    for col in cat_features:
        if df[col].nunique() == 0:
            continue

        top_classes = df[col].value_counts(normalize=True).to_dict()

        cat_stats.append({
            'Feature': col,
            'Unique Classes': df[col].nunique(),
            'Missing Values': df[col].isnull().sum(),
            'Class Proportions': top_classes
        })

    return cat_stats

def save_statistics_to_csv(df, directory = "output", numeric_filename='numeric_statistics.csv',
                           categorical_filename='categorical_statistics.csv', numeric_categories = None, categorical_categories = None,):
    os.makedirs(directory, exist_ok=True)

    numeric_stats = get_numeric_statistics(df, numeric_categories)
    categorical_stats = get_categorical_statistics(df, categorical_categories)

    numeric_stats.to_csv(f"{directory}/{numeric_filename}", sep=';', index=True)
    pd.DataFrame(categorical_stats).to_csv(f"{directory}/{categorical_filename}", sep=';', index=False)


