import matplotlib.pyplot as plt
import seaborn as sns
import os


def plot_previous_qualification_by_target(df):
    plt.figure(figsize=(12, 7))
    sns.histplot(data=df, x="Previous qualification (grade)", hue="Target", multiple="stack", bins=15, palette="Set2")
    plt.title("Distribution of Previous Qualification (Grade) by Target")
    plt.xlabel("Previous Qualification (Grade)")
    plt.tight_layout()
    plt.savefig('plots/histograms/previous_qualification_by_target.png', dpi=300)
    plt.close()


def plot_percentage_of_enrolled_by_gdp(df):
    df_long = df.groupby('GDP')['Target'].value_counts(normalize=True).mul(100).reset_index(name='Percentage')
    df_long = df_long.query("Target == 'Enrolled'").drop(columns='Target')

    plt.figure(figsize=(14, 7))
    sns.histplot(x="GDP", weights="Percentage", data=df_long, color="blue", bins=30)
    sns.regplot(x=df_long["GDP"].astype(float), y="Percentage", data=df_long, scatter=False, color="red", ci=95,
                line_kws={'linewidth': 2, 'linestyle': '--'})

    plt.xlabel("GDP", fontsize=12)
    plt.ylabel("Percentage of Enrolled", fontsize=12)
    plt.title("Percentage of Enrolled by GDP with Trend Line", fontsize=14, fontweight='bold')
    plt.ylim(df_long["Percentage"].min() - 3, df_long["Percentage"].max() + 3)
    plt.tight_layout()
    plt.savefig('plots/histograms/percentage_of_enrolled_by_gdp.png', dpi=300)
    plt.close()


def plot_students_distribution_by_units(df):
    students_with_passing_grades = df.loc[df['Curricular units 2nd sem (grade)'] > 5]
    plt.figure(figsize=(14, 7))
    sns.histplot(x="Curricular units 2nd sem (grade)", data=students_with_passing_grades, color="blue")
    plt.title("Distribution of Students by 2nd Semester Unit Grades", fontsize=14, fontweight='bold')
    plt.xlabel("Grades in 2nd Semester Units", fontsize=12)
    plt.ylabel("Number of Students", fontsize=12)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig('plots/histograms/students_distribution_by_units.png', dpi=300)
    plt.close()


def generate_hist_plots(df):
    os.makedirs('../plots/histograms', exist_ok=True)
    plot_previous_qualification_by_target(df)
    plot_percentage_of_enrolled_by_gdp(df)
    plot_students_distribution_by_units(df)
