import os

import matplotlib.pyplot as plt
import seaborn as sns


def plot_target_vs_course(df):
    course_target_distribution = df.groupby("Course Text")["Target"].value_counts(normalize=True).mul(100).reset_index(name="Percentage")
    plt.figure(figsize=(14, 7))
    sns.set_theme(style="whitegrid")
    sns.barplot(x="Course Text",y="Percentage",hue="Target", data=course_target_distribution, palette="coolwarm")
    plt.title("Percentage Distribution of Student Statuses by Course", fontsize=14, fontweight="bold")
    plt.xlabel("Course", fontsize=12)
    plt.ylabel("Percentage of Students", fontsize=12)
    plt.xticks(rotation=45, ha="right")
    plt.legend(title="Student Status")
    plt.tight_layout()
    plt.savefig('plots/barplots/target_vs_course.png', dpi=300)
    plt.close()


def plot_inflation_vs_daytime_attendance(df):
    df_long = df.groupby('Inflation rate', as_index=False)['Daytime/evening attendance'].mean()
    df_long.rename(columns={'Daytime/evening attendance': 'Mean'}, inplace=True)

    plt.figure(figsize=(14, 7))
    sns.barplot(x="Inflation rate", y="Mean", palette="viridis", data=df_long, edgecolor="black", hue="Inflation rate",
                legend=False)
    plt.xlabel("Inflation rate", fontsize=12)
    plt.ylabel("Daytime attendance", fontsize=12)
    plt.tight_layout()
    plt.savefig('plots/barplots/inflation_vs_daytime_attendance.png', dpi=300)
    plt.close()


def generate_barplots(df):
    os.makedirs('plots/barplots', exist_ok=True)
    plot_inflation_vs_daytime_attendance(df)
    plot_target_vs_course(df)
