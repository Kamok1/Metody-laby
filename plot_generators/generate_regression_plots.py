import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot_linear_regression(df):
    plt.figure(figsize=(14, 7))
    sns.regplot(x="Age at enrollment", y="Curricular units 1st sem (grade)", data=df, scatter_kws={'s': 50, 'color': 'blue'}, line_kws={'color': 'red'}, ci=90)
    plt.title("Linear Regression between Age and Grade with Error Bars")
    plt.xlabel("Age")
    plt.ylabel("Grade")
    plt.tight_layout()
    plt.savefig('plots/regressions/linear_regression_age_grade.png', dpi=300)
    plt.close()

def plot_filtered_linear_regression(df):
    df["Filtred Grade"] = df["Curricular units 1st sem (grade)"].where(df["Curricular units 1st sem (grade)"] > 0)
    plt.figure(figsize=(14, 7))
    sns.regplot(x="Age at enrollment", y="Filtred Grade", data=df, scatter_kws={'s': 50, 'color': 'blue'}, line_kws={'color': 'red'}, ci=90)
    plt.title("Filtred Linear Regression between Age and Grade with Error Bars")
    plt.xlabel("Age")
    plt.ylabel("Grade")
    plt.tight_layout()
    plt.savefig('plots/regressions/filtred_linear_regression_age_grade.png', dpi=300)
    plt.close()

def plot_filtered_average_proportion(df):
    age_group_stats = df.groupby('Age at enrollment').agg(
        count=('Target encoded', 'size'),
        mean=('Target encoded', 'mean'),
    ).reset_index()
    age_group_filtered = age_group_stats[age_group_stats['count'] > 10]

    plt.figure(figsize=(14, 7))
    sns.regplot(x="Age at enrollment", y="mean", data=age_group_filtered, scatter_kws={'s': 50, 'color': 'blue', 'alpha': 0.6},
                line_kws={'color': 'red', 'linewidth': 2, 'linestyle': '--'}, ci=90)
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.title("Linear Regression for Average 'Graduate' Proportion vs Age at Enrollment (Filtered)")
    plt.xlabel("Age at Enrollment")
    plt.ylabel("Proportion of Graduates (1 = Graduate, -1 = Dropout)")
    plt.tight_layout()
    plt.savefig('plots/regressions/average_graduate_proportion_vs_age.png', dpi=300)
    plt.close()

def generate_regression_plots(df):
    os.makedirs('../plots/regressions', exist_ok=True)
    plot_linear_regression(df)
    plot_filtered_linear_regression(df)
    plot_filtered_average_proportion(df)
