import pandas as pd 
df =pd.read_csv(r"C:\Users\hemam\OneDrive\Desktop\mutual_fund_analytics\data\raw\08_investor_transactions.csv")
print(df.duplicated().sum())
df=df.drop_duplicates()
df['transaction_date'] = pd.to_datetime(
    df['transaction_date'],
    dayfirst=True,
    errors='coerce'
)
print(df['transaction_date'].isnull().sum())
print(df['transaction_type'].unique())
print((df['amount_inr'] <= 0).sum())
print(df['gender'].unique())
print(df['age_group'].unique())
print(df['city_tier'].unique())
print(df['kyc_status'].unique())
print((df['annual_income_lakh'] <= 0).sum())
print(df['payment_mode'].unique())
df.to_csv(
    "../data/processed/investor_transactions_cleaned.csv",
    index=False
)

print("Saved Successfully!")