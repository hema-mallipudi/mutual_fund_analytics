import pandas as pd
df=pd.read_csv(r"C:\Users\hemam\OneDrive\Desktop\mutual_fund_analytics\data\raw\01_fund_master.csv")
print(df.head())
print(df.shape)
print(df.columns)
print(df.isnull().sum())
print(df.duplicated().sum())
#converting launch date to datetime
df['launch_date']=pd.to_datetime(df['launch_date'],errors='coerce')
print(df['launch_date'].isnull().sum())
#validate amfi codes
print(df['amfi_code'].duplicated().sum())
#clean text columns
text_cols = [
    'fund_house',
    'scheme_name',
    'category',
    'sub_category',
    'plan',
    'benchmark',
    'fund_manager',
    'risk_category',
    'sebi_category_code'
]
for col in text_cols:
    df[col] = df[col].str.strip()
#validate expense ratio
invalid_expense = df[
    (df['expense_ratio_pct'] < 0.1) |
    (df['expense_ratio_pct'] > 2.5)
]
print(invalid_expense)
#validate exit_load
print((df['exit_load_pct'] < 0).sum())
#validate SIP load
print((df['min_sip_amount'] <= 0).sum())
#validate lumpsum amount
print((df['min_lumpsum_amount'] <= 0).sum())
#check risk category
print(df['risk_category'].unique())
df.to_csv(r"C:\Users\hemam\OneDrive\Desktop\mutual_fund_analytics\data\processed\fund_master_cleaned.csv" , index=False)
