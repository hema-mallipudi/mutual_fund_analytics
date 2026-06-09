import pandas as pd
df = pd.read_csv(r"C:\Users\hemam\OneDrive\Desktop\mutual_fund_analytics\data\raw\10_benchmark_indices.csv")
print(df.isnull().sum())
print("Duplicates:", df.duplicated().sum())
df = df.drop_duplicates()
df['date'] = pd.to_datetime(
    df['date'], format='%Y-%m-%d')
df['index_name'] = (
    df['index_name']
    .str.strip()
)
df.to_csv(r"C:\Users\hemam\OneDrive\Desktop\mutual_fund_analytics\data\processed\10_benchmark_indices_cleaned.csv",index=False)
print("Saved Successfully")