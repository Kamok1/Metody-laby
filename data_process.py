import pandas as pd

from constants import *


def map_education_levels(df):
    education_mapping = {
        34:0, 35: 1, 36: 2, 37: 3, 26: 4, 11: 5, 30: 6, 29: 7, 14: 8, 10: 9, 12: 10, 13: 11, 20: 12, 25: 13, 18: 14, 31: 15, 33: 16, 27: 17, 38: 18, 19: 19, 9: 20, 1: 21, 22: 22, 6: 23, 39: 24, 40: 25, 2: 26, 3: 27, 41: 28, 42: 29, 4: 30, 43: 31, 5: 32, 44: 33
    }
    df["Mother's qualification level"] = df["Mother's qualification"].map(education_mapping)
    df["Father's qualification level"] = df["Father's qualification"].map(education_mapping)
    return df



def categorize_qualification(qualification):
    if qualification in [35, 36]:
        return 'No Literacy / Very Basic'
    elif qualification in [37, 26, 11, 30, 29, 38]:
        return 'Basic Education'
    elif qualification in [14, 10, 12, 27, 19, 9, 1]:
        return 'Secondary Education'
    elif qualification in [13, 20, 25, 18, 22, 31, 33]:
        return 'Complementary / Technical Secondary'
    elif qualification in [2, 3, 4, 5, 40, 43, 44]:
        return 'Higher Education - Academic'
    elif qualification in [6, 39, 41, 42]:
        return 'Higher Education - Professional'
    else:
        return 'Other / Unknown'



def generate_target_encoded(df):
    df['Target encoded'] = df['Target'].apply(lambda x: 1 if x == 'Graduate' else (-1 if x == 'Dropout' else None))
    return df

def categorize_mothers_qualification(df):
    df['Mother\'s qualification category'] = df['Mother\'s qualification'].apply(categorize_qualification)
    return df

def add_text_columns(df):
    df['Marital Status Text'] = df['Marital status'].map(marital_status_map)
    df['Application mode Text'] = df['Application mode'].map(application_mode_map)
    df['Course Text'] = df['Course'].map(course_map).fillna("Unknown Course")
    df['Daytime/evening attendance Text'] = df['Daytime/evening attendance'].map(daytime_evening_attendance_map)
    df['Previous qualification Text'] = df['Previous qualification'].map(previous_qualification_map)
    df['Nacionality Text'] = df['Nacionality'].map(nationality_map)
    df['Mother\'s qualification Text'] = df['Mother\'s qualification'].map(mothers_qualification_map)
    df['Father\'s qualification Text'] = df['Father\'s qualification'].map(fathers_qualification_map)
    df['Mother\'s occupation Text'] = df['Mother\'s occupation'].map(mothers_occupation_map)
    df['Father\'s occupation Text'] = df['Father\'s occupation'].map(fathers_occupation_map)
    df['Gender Text'] = df['Gender'].map(gender_map)
    df['Displaced Text'] = df['Displaced'].map(bool_map)
    df['Educational special needs Text'] = df['Educational special needs'].map(bool_map)
    df['Debtor Text'] = df['Debtor'].map(bool_map)
    df['Tuition fees up to date Text'] = df['Tuition fees up to date'].map(bool_map)
    df['Scholarship holder Text'] = df['Scholarship holder'].map(bool_map)
    df['International Text'] = df['International'].map(bool_map)
    return df

def process_education_data(df):
    df = map_education_levels(df)
    df = categorize_mothers_qualification(df)
    df = generate_target_encoded(df)
    df = add_text_columns(df)
    return df