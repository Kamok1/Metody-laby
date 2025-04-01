import os
import matplotlib.pyplot as plt
import seaborn as sns


def plot_age_distribution(df):
    plt.figure(figsize=(14, 7))
    sns.countplot(x="Age at enrollment", data=df, palette="Set2", hue="Age at enrollment", legend=False)
    plt.title("Distribution of Students by Age at Enrollment", fontsize=14, fontweight="bold")
    plt.xlabel("Age at Enrollment", fontsize=12)
    plt.ylabel("Number of Students", fontsize=12)

    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig('plots/countplots/age_distribution.png', dpi=300)
    plt.close()


def plot_course_distribution(df):
    plt.figure(figsize=(14, 7))
    sns.countplot(x="Course Text", data=df, palette="Set2", hue="Course Text", legend=False)
    plt.title("Distribution of Students by Course", fontsize=14, fontweight="bold")
    plt.xlabel("Course Name", fontsize=12)
    plt.ylabel("Number of Students", fontsize=12)
    plt.xticks(rotation=90)
    plt.tight_layout()

    plt.savefig('plots/countplots/course_distribution.png', dpi=300)
    plt.close()


def plot_target_by_debtor(df):
    plt.figure(figsize=(14, 7))
    sns.countplot(x="Target", data=df, palette="Set2", hue="Debtor")

    plt.title("Count of Target Categories by Debtor Status", fontsize=14, fontweight="bold")
    plt.xlabel("Target Category", fontsize=12)
    plt.ylabel("Count of Target", fontsize=12)

    legend_labels = ["No" if text == "0" else "Yes" for text in df["Debtor"].astype(str).unique()]
    plt.legend(title="Debtor", labels=legend_labels)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('plots/countplots/target_by_debtor.png', dpi=300)
    plt.close()


def generate_countplots(df):
    os.makedirs('plots/countplots', exist_ok=True)
    plot_target_by_debtor(df)
    plot_age_distribution(df)
    plot_course_distribution(df)
