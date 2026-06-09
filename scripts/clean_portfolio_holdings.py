import pandas as pd 
df=pd.read_csv(r"C:\Users\hemam\OneDrive\Desktop\mutual_fund_analytics\data\raw\09_portfolio_holdings.csv")
print(df.isnull().sum())
print("Duplicates:",df.duplicated().sum())
df = df.drop_duplicates()
df['portfolio_date'] = pd.to_datetime(
    df['portfolio_date'],  format='%Y-%m-%d')
df.to_csv(
    r"C:\Users\hemam\OneDrive\Desktop\mutual_fund_analytics\data\processed\portfolio_holdings_cleaned.csv",
    index=False
)
print("portfolio_holdings_cleaned.csv saved successfully")