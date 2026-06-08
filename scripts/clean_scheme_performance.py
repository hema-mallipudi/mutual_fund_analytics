import pandas as pd
df=pd.read_csv(r"C:\Users\hemam\OneDrive\Desktop\mutual_fund_analytics\data\raw\07_scheme_performance.csv")
print(df.head())
print(df.shape)
print(df.columns)
print(df.isnull().sum())
print(df.duplicated().sum())
return_cols=['return_1yr_pct','return_3yr_pct','return_5yr_pct']
for col in return_cols:
    df[col] = pd.to_numeric(
        df[col],
        errors='coerce')
for col in return_cols:
    print(col)
    print(df[col].isnull().sum())
#anomaly flag
for col in return_cols:
    df[f'{col}_anomaly'] = (
        (df[col] < -100) |
        (df[col] > 100)
    )
#count anomalies
for col in return_cols:
    print(
        col,
        df[f'{col}_anomaly'].sum()
    )
#check expenses
print(df['expense_ratio_pct'].describe())
df['expense_ratio_pct'] = pd.to_numeric(
    df['expense_ratio_pct'],
    errors='coerce'
)
invalid_expense = df[
    (df['expense_ratio_pct'] < 0.1) |
    (df['expense_ratio_pct'] > 2.5)
]
print(invalid_expense)
print(
    "Invalid Expense Ratio Rows:",
    len(invalid_expense)
)
df['expense_ratio_valid'] = (
    (df['expense_ratio_pct'] >= 0.1) &
    (df['expense_ratio_pct'] <= 2.5)
)
print(
    df['expense_ratio_valid']
    .value_counts()
)
print(df.duplicated().sum())

df = df.drop_duplicates()

df.to_csv(r"C:\Users\hemam\OneDrive\Desktop\mutual_fund_analytics\data\processed\scheme_performance_cleaned.csv",index=False)