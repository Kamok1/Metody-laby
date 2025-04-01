import os
import matplotlib.pyplot as plt
import seaborn as sns

def encode_target(df):
    df['Target encoded'] = df['Target'].apply(lambda x: 1 if x == 'Graduate' else (-1 if x == 'Dropout' else None))


def calculate_correlation_matrix(df):
    encode_target(df)
    numeric_df = df.select_dtypes(include='number')
    return numeric_df.corr()


def plot_filtered_corr_matrix(correlation_matrix, keys=None):
    os.makedirs('plots/heatmaps', exist_ok=True)

    if keys is None:
        keys = correlation_matrix.columns.tolist()

    keys = [key for key in keys if key in correlation_matrix.columns]

    if not keys:
        print("Brak odpowiednich zmiennych do analizy korelacji.")
        return

    filtered_corr_matrix = correlation_matrix.loc[keys, keys]

    plt.figure(figsize=(14, 7))
    sns.heatmap(filtered_corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
    plt.title("Selected Correlations Heatmap")
    plt.tight_layout()
    plt.savefig('plots/heatmaps/selected_correlations_heatmap.png', dpi=300)
    plt.close()


def generate_heatmaps(df):
    keys = ['Target encoded', 'GDP', "Mother's qualification level", 'Course',
            'Daytime/evening attendance', 'Curricular units 1st sem (grade)', 'Age at enrollment',
            'Unemployment rate', 'Marital Status', "Father's qualification level",
            'Curricular units 2nd sem (credited)', 'Curricular units 1st sem (credited)', 'Gender']

    correlation_matrix = calculate_correlation_matrix(df)
    plot_filtered_corr_matrix(correlation_matrix, keys)
