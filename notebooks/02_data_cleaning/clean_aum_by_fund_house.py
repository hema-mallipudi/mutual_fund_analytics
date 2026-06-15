import pandas as pd
aum_df = pd.read_csv(r"C:\Users\hemam\OneDrive\Desktop\mutual_fund_analytics\data\raw\03_aum_by_fund_house.csv")
print(aum_df.head())
print(aum_df.info())
print(aum_df.isnull().sum())
aum_df = aum_df.dropna()
print("Duplicates:",aum_df.duplicated().sum())
aum_df['date'] = pd.to_datetime(
    aum_df['date'],
    dayfirst=True,
    errors='coerce'
)
print(aum_df['date'].isnull().sum())
aum_df['fund_house'] = (
    aum_df['fund_house']
    .str.strip()
)
print(aum_df['fund_house'].unique())
print(
    (aum_df['aum_lakh_crore'] <= 0).sum()
)
#validate aum value
print((aum_df['aum_crore'] <= 0).sum())
#validate number of schemes
print((aum_df['num_schemes'] <= 0).sum())
#verify sbi dominance
sbi_df = aum_df[
    aum_df['fund_house']
    .str.contains('SBI')
]
print(sbi_df[['date','aum_lakh_crore']])
aum_df.to_csv(
    "../data/processed/aum_by_fund_house_cleaned.csv",index=False)
print("aum_by_fund_house_cleaned.csv saved successfully")