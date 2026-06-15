import pandas as pd
df = pd.read_csv(
    "../data/raw/06_industry_folio_count.csv"
)
print(df.isnull().sum())
print("Duplicates:",df.duplicated().sum())
df['month'] = pd.to_datetime(
    df['month']
)
df.to_csv(
    "../data/processed/industry_folio_count_cleaned.csv",
    index=False
)