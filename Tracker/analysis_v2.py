# tracker/functions.py
import os
import csv

"""Dataset analysis - load, clean, and summarize the project dataset."""
import pandas as pd

CSV_PATH = "data/sample_records_250.csv"


#def load_dataset(path=CSV_PATH):
    # TODO: اقرا الملف وارجع النتيجة
#    pass


#def clean_dataset(df):
    # TODO: drop_duplicates ثم اتعامل مع النواقص
    # (احذف النواقص أو عوّضها — واكتب قرارك في التقرير)
 #   pass


#def summary_by_category(df, category_col, value_col):
    # TODO: groupby + mean
#    pass



def load_dataset(path=CSV_PATH):
    """Reads the CSV file into a pandas DataFrame."""
    if not os.path.exists(path):
        print(f"Error: File not found at {path}")
        return pd.DataFrame()
    return pd.read_csv(path)




def clean_dataset(df):
    """Removes duplicates and handles missing values."""
    if df.empty:
        return df

    # إزالة الصفوف المكررة بالكامل
    df_cleaned = df.drop_duplicates()

    # التعامل مع القيم الناقصة (ملء القيم الفارغة في الحقول النصية بـ 'Unknown' والرقمية بـ المتوسط)
    for col in df_cleaned.columns:
        if df_cleaned[col].isnull().any():
            if df_cleaned[col].dtype in ['float64', 'int64']:
                df_cleaned[col] = df_cleaned[col].fillna(df_cleaned[col].mean())
            else:
                df_cleaned[col] = df_cleaned[col].fillna('Unknown')

    return df_cleaned


def summary_by_category(df, category_col, value_col):
    """Groups by category_col and calculates the mean of value_col."""
    if df.empty or category_col not in df.columns or value_col not in df.columns:
        return pd.DataFrame()

    # تجميع البيانات وحساب المتوسط لكل تصنيف
    summary_df = df.groupby(category_col)[value_col].mean().reset_index()
    return summary_df


def count_by_category(df, category_col):
    """Groups by category_col and calculates the count of occurrences."""
    if df.empty or category_col not in df.columns:
        return pd.DataFrame()

    # تجميع البيانات وحساب العدد لكل تصنيف
    count_df = df.groupby(category_col).size().reset_index(name='issue_count')
    return count_df





df_raw = load_dataset()
print(f"Raw dataset shape: {df_raw.shape}")



df_clean = clean_dataset(df_raw)
print(f"Cleaned dataset shape: {df_clean.shape}")



cleaned_file_path = "data/cleaned_sample_records_250.csv"
df_clean.to_csv(cleaned_file_path, index=False)
print(f"تم حفظ الملف بنجاح في المسار: {cleaned_file_path}")


