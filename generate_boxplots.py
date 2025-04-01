import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot_mothers_qualification_vs_grade(df):
    plt.figure(figsize=(20, 15))
    sns.boxplot(x="Mother's qualification category", y="Curricular units 2nd sem (grade)", data=df, palette='pastel', hue="Mother's qualification category", legend=False)
    plt.title("Mother's Qualification Category vs Curricular Units 2nd Sem (Grade)")
    plt.xticks(rotation=45, ha="right")
    plt.ylim(df["Curricular units 2nd sem (grade)"].min(), df["Curricular units 2nd sem (grade)"].max())
    plt.tight_layout()
    plt.savefig('plots/boxplots/mothers_qualification_vs_grade.png', dpi=300)
    plt.close()

def plot_age_at_enrollment(df):
    plt.figure(figsize=(14, 7))
    sns.boxplot(x="Target", y="Age at enrollment", data=df, palette="pastel", hue="Target")
    plt.title("Distribution of Age at Enrollment Across Target Categories")
    plt.xlabel("Target Category (Dropout, Graduate, Enrolled)")
    plt.ylabel("Age at Enrollment")
    plt.ylim(16, 50)
    plt.tight_layout()
    plt.savefig('plots/boxplots/age_at_enrollment.png', dpi=300)
    plt.close()

def plot_mothers_qualification_level_vs_grade(df):
    plt.figure(figsize=(40, 20))
    sns.boxplot(x="Mother's qualification level", y="Curricular units 2nd sem (grade)", data=df, palette='Set1', hue="Mother's qualification level", legend=False)
    plt.title("Mother's Qualification Level vs Curricular Units 2nd Sem (Grade)")
    plt.ylim(0, 18)
    plt.tight_layout()
    plt.savefig('plots/boxplots/mothers_qualification_level_vs_grade.png', dpi=300)
    plt.close()

def generate_boxplots(df):
    os.makedirs('plots/boxplots', exist_ok=True)
    plot_mothers_qualification_vs_grade(df)
    plot_age_at_enrollment(df)
    plot_mothers_qualification_level_vs_grade(df)
