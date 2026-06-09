import pandas as pd
df=pd.read_csv(r"C:\Users\hemam\OneDrive\Desktop\mutual_fund_analytics\data\raw\05_category_inflows.csv")
print(df.head())
print(df.shape)
print("rows:",df.shape[0])
print("columns:",df.shape[1])
print(df.columns)
print(df.isnull().sum())
print(df.duplicated().sum())
df['month'] = pd.to_datetime(
    df['month']
)
df.to_csv("../data/processed/category_inflows_cleaned.csv",index=False)
print("Saved Successfully!")