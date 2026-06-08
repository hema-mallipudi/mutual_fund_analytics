import pandas as pd
from sqlalchemy import create_engine
engine = create_engine(
    "sqlite:///../database/mutual_fund_analytics.db")
print("Database connected successfully!")

import pandas as pd
from sqlalchemy import create_engine

# Load CSV files
nav_df = pd.read_csv(r"C:\Users\hemam\OneDrive\Desktop\mutual_fund_analytics\data\processed\nav_history_cleaned.csv")
txn_df = pd.read_csv(r"C:\Users\hemam\OneDrive\Desktop\mutual_fund_analytics\data\processed\investor_transaction_cleaned.csv")
perf_df = pd.read_csv(r"C:\Users\hemam\OneDrive\Desktop\mutual_fund_analytics\data\processed\scheme_performance_cleaned.csv")
# Load into SQLite tables
nav_df.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)
txn_df.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)
perf_df.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)
print("All datasets loaded successfully!")
print("fact_nav:", len(nav_df))
print("fact_transactions:", len(txn_df))
print("fact_performance:", len(perf_df))