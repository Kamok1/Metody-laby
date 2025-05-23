import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

def plot_unemployment_rate_distribution(df):
    plt.figure(figsize=(14, 7))
    sns.violinplot(x="Target", y="Unemployment rate", data=df, palette="Set2", dodge=False, hue="Target")
    plt.title("Distribution of Unemployment Rate Across Target Categories")
    plt.xlabel("Target Category (Dropout, Graduate, Enrolled)")
    plt.ylabel("Unemployment Rate")
    plt.ylim(df["Unemployment rate"].min(), df["Unemployment rate"].max())
    plt.savefig('plots/violinplots/unemployment_rate_distribution.png', dpi=300)
    plt.close()

def plot_grade_distribution_by_gender(df):
    plt.figure(figsize=(14, 7))
    sns.violinplot( x="Gender Text", y="Curricular units 1st sem (grade)", data=df, palette="Set2", hue="Gender Text",
                     legend=False, dodge=True, split=True)
    plt.title("Distribution of 1st Semester Grades by Gender")
    plt.xlabel("Gender")
    plt.ylabel("Grade (1st Semester)")
    plt.ylim(df["Curricular units 1st sem (grade)"].min(), df["Curricular units 1st sem (grade)"].max())
    plt.savefig('plots/violinplots/grade_distribution_by_gender.png', dpi=300)
    plt.close()

def plot_grade_distribution_by_age_group(df):
    df['Age Group'] = pd.cut(df['Age at enrollment'], bins=[18, 21, 26, 35, 65], labels=['18-21', '22-26', '27-35', '36-65'])
    plt.figure(figsize=(14, 7))
    sns.violinplot(x="Age Group", y="Curricular units 2nd sem (grade)", data=df, palette="Set2", hue="Age Group", legend=False)
    age_group_counts = df['Age Group'].value_counts(normalize=True) * 100
    max_grade = df["Curricular units 2nd sem (grade)"].max()
    for i, age_group in enumerate(age_group_counts.index):
        plt.text(i, max_grade + 1, f'{age_group_counts[age_group]:.2f}%', horizontalalignment='center', size=8, color='black', weight='semibold')
    plt.title("Grade Distribution by Age Group with Percentages")
    plt.ylabel("Grade")
    plt.ylim(df["Curricular units 2nd sem (grade)"].min(), max_grade)
    plt.savefig('plots/violinplots/grade_distribution_by_age_group.png', dpi=300)
    plt.close()

def generate_violinplots(df):
    os.makedirs('../plots/violinplots', exist_ok=True)
    plot_unemployment_rate_distribution(df)
    plot_grade_distribution_by_age_group(df)
    plot_grade_distribution_by_gender(df)
