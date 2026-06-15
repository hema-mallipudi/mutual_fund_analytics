import pandas as pd

# Load scheme performance data
performance = pd.read_csv(r"C:\Users\hemam\OneDrive\Desktop\mutual_fund_analytics\data\processed\07_scheme_performance_cleaned.csv")

# User input
risk_appetite = input(
    "Enter Risk Appetite (Moderate / Very High / Low / High / Moderately High): "
)

# Top 3 funds by Sharpe Ratio
recommendations = (
    performance[
        performance['risk_grade'].str.lower()
        == risk_appetite.lower()
    ]
    .sort_values(
        by='sharpe_ratio',
        ascending=False
    )
    .head(3)
)

print("\nTop 3 Recommended Funds:\n")

print(
    recommendations[
        [
            'scheme_name',
            'fund_house',
            'category',
            'risk_grade',
            'sharpe_ratio'
        ]
    ]
)