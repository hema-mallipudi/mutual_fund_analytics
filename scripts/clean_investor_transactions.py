import pandas as pd
df=pd.read_csv(r"C:\Users\hemam\OneDrive\Desktop\mutual_fund_analytics\data\raw\08_investor_transactions.csv")
print(df.head())
print(df.shape)
print("rows:",df.shape[0])
print("columns:",df.shape[1])
print(df.columns)
print(df.isnull().sum())
print(df.duplicated().sum())
#standardize
print(df['transaction_type'].unique())
#invalid amount
invalid_amount=df[df['amount_inr']<=0]
print(invalid_amount)
print(len(invalid_amount))
#fix date formats
import pandas as pd
df['transaction_date']=pd.to_datetime(df['transaction_date'],errors='coerce')
print(df['transaction_date'].isnull().sum())
print(df['kyc_status'].unique())
print(df.duplicated().sum())
#saving
df.to_csv(r"C:\Users\hemam\OneDrive\Desktop\mutual_fund_analytics\data\processed\investor_transaction_cleaned.csv", index=False)
