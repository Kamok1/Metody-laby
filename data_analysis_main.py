import os
import pandas as pd
from data_process import process_data
from data_summary import save_statistics_to_csv
from generate_barplots import generate_barplots
from generate_boxplots import generate_boxplots
from generate_corelations import generate_heatmaps
from generate_countplots import generate_countplots
from generate_histogram_plots import generate_hist_plots
from generate_pca import plot_pca
from generate_regression_plots import generate_regression_plots
from generate_violinplots import generate_violinplots


def load_dataset(path, sep=';'):
    df = pd.read_csv(path, sep=sep, low_memory=False)
    return df

def main():
    df = load_dataset("data/students.csv", sep=";")

    os.makedirs("plots", exist_ok=True)

    process_data(df)
    save_statistics_to_csv(df, numeric_categories=['Application order', 'Previous qualification (grade)',
                                                   'Age at enrollment',
                                                   'Admission grade',
                                                   'Curricular units 1st sem (credited)',
                                                   'Curricular units 1st sem (enrolled)',
                                                   'Curricular units 1st sem (evaluations)',
                                                   'Curricular units 1st sem (approved)',
                                                   'Curricular units 1st sem (grade)',
                                                   'Curricular units 1st sem (without evaluations)',
                                                   'Curricular units 2nd sem (credited)',
                                                   'Curricular units 2nd sem (enrolled)',
                                                   'Curricular units 2nd sem (evaluations)',
                                                   'Curricular units 2nd sem (approved)',
                                                   'Curricular units 2nd sem (grade)',
                                                   'Unemployment rate', "Mother's qualification level",
                                                   "Father's qualification level"],
                           categorical_categories=[
                                                   'Displaced',
                                                   'Educational special needs',
                                                   'Debtor',
                                                   'Tuition fees up to date',
                                                   'Gender',
                                                   'Scholarship holder',
                                                   'International',
                                                   'Unemployment rate',
                                                   'Inflation rate',
                                                   'Course Text',
                                                   'GDP',
                                                   'Target',
                                                   'Mother\'s qualification category',
                                                   'Marital Status Text',
                                                   'Application mode Text',
                                                   'Daytime/evening attendance Text',
                                                   'Previous qualification Text',
                                                   'Nacionality Text',
                                                   "Mother's qualification Text",
                                                   "Father's qualification Text",
                                                   "Mother's occupation Text", "Father's occupation Text", ])
    generate_barplots(df)
    generate_boxplots(df)
    generate_heatmaps(df)
    generate_countplots(df)
    generate_hist_plots(df)
    generate_regression_plots(df)
    generate_violinplots(df)
    plot_pca(df, attributes=['Previous qualification', 'Previous qualification (grade)', 'Admission grade', 'Scholarship holder',
                  'Gender', 'Debtor', 'Age at enrollment', 'Curricular units 1st sem (credited)',
                  'Curricular units 1st sem (enrolled)', 'Curricular units 1st sem (evaluations)',
                  'Curricular units 1st sem (approved)', 'Curricular units 1st sem (grade)',
                  'Curricular units 1st sem (without evaluations)', 'Curricular units 2nd sem (credited)',
                  'Curricular units 2nd sem (enrolled)', 'Curricular units 2nd sem (evaluations)',
                  'Curricular units 2nd sem (approved)', 'Curricular units 2nd sem (grade)',
                  'Curricular units 2nd sem (without evaluations)', "Mother's qualification level", "Father's qualification level"])


if __name__ == "__main__":
    main()