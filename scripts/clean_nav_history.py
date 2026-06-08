import pandas as pd 
df = pd.read_csv(r"C:\Users\hemam\OneDrive\Desktop\mutual_fund_analytics\data\raw\02_nav_history.csv")
print(df.head())
print(df.shape)
print(df.dtypes)
print("rows:" ,df.shape[0])
print("columns:",df.shape[1])
print(df.columns)
print("null values",df.isnull().sum())
print("duplicates",df.duplicated().sum())
df['date']=pd.to_datetime(df['date'],errors='coerce')
print(df['date'].dtype)
print(df['date'].isnull().sum())
df=df.sort_values(by=['amfi_code','date'])
print(df.head())
print(df['nav'].isnull().sum())
df.to_csv(r"C:\Users\hemam\OneDrive\Desktop\mutual_fund_analytics\data\processed\nav_history_cleaned.csv",
    index=False
)