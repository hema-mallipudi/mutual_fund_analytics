# Mutual Fund Analytics Project – Data Dictionary

## Project Overview

This data dictionary documents the datasets used in the Mutual Fund Analytics Project. It includes column names, data types, business definitions, and source dataset references.

---

# Dataset 1: Fund Master

**Source File:** `01_fund_master.csv`

| Column Name        | Data Type | Business Definition                                       
| amfi_code          | INTEGER   | Unique AMFI identifier for each mutual fund scheme              |
| fund_house         | TEXT      | Name of the Asset Management Company (AMC)                      |
| scheme_name        | TEXT      | Name of the mutual fund scheme                                  |
| category           | TEXT      | Broad category of the fund (Equity, Debt, Hybrid, etc.)         |
| sub_category       | TEXT      | Detailed classification within the category                     |
| plan               | TEXT      | Plan type (Regular/Direct)                                      |
| launch_date        | DATE      | Date on which the scheme was launched                           |
| benchmark          | TEXT      | Benchmark index used to evaluate fund performance               |
| expense_ratio_pct  | REAL      | Annual management fee charged by the fund (%)                   |
| exit_load_pct      | REAL      | Fee charged when investors redeem before a specified period (%) |
| min_sip_amount     | REAL      | Minimum amount required for SIP investment                      |
| min_lumpsum_amount | REAL      | Minimum amount required for lump sum investment                 |
| fund_manager       | TEXT      | Name of the fund manager                                        |
| risk_category      | TEXT      | Risk classification of the scheme                               |
| sebi_category_code | TEXT      | SEBI classification code                                        |

---

# Dataset 2: NAV History

**Source File:** `02_nav_history.csv`

| Column Name | Data Type | Business Definition                                 |
| ----------- | --------- | --------------------------------------------------- |
| amfi_code   | INTEGER   | Mutual fund identifier                              |
| date        | DATE      | NAV reporting date                                  |
| nav         | REAL      | Net Asset Value of the scheme on the specified date |

### Business Notes

* NAV represents per-unit value of the mutual fund.
* Missing NAV values on holidays/weekends were forward-filled during cleaning.

---

# Dataset 3: Scheme Performance

**Source File:** `07_scheme_performance.csv`

| Column Name       | Data Type | Business Definition                     |
| ----------------- | --------- | --------------------------------------- |
| amfi_code         | INTEGER   | Mutual fund identifier                  |
| one_year_return   | REAL      | Scheme return over the last 1 year (%)  |
| three_year_return | REAL      | Scheme return over the last 3 years (%) |
| five_year_return  | REAL      | Scheme return over the last 5 years (%) |
| expense_ratio     | REAL      | Annual expense ratio (%)                |

### Business Notes

* Return values are stored as percentages.
* Expense ratio validation range: 0.1% – 2.5%.

---

# Dataset 4: Investor Transactions

**Source File:** `08_investor_transactions.csv`

| Column Name      | Data Type | Business Definition                            |
| ---------------- | --------- | ---------------------------------------------- |
| transaction_id   | INTEGER   | Unique transaction identifier                  |
| investor_id      | INTEGER   | Unique investor identifier                     |
| amfi_code        | INTEGER   | Mutual fund identifier                         |
| transaction_date | DATE      | Date of transaction                            |
| transaction_type | TEXT      | Type of transaction (SIP, Lumpsum, Redemption) |
| amount           | REAL      | Transaction amount in INR                      |
| kyc_status       | TEXT      | Investor KYC verification status               |

### Valid Values

#### transaction_type

* SIP
* Lumpsum
* Redemption

#### kyc_status

* Verified
* Pending
* Rejected

---

# SQLite Star Schema Tables

## Dimension Table: dim_fund

| Column Name  | Data Type | Description              |
| ------------ | --------- | ------------------------ |
| fund_id      | INTEGER   | Surrogate primary key    |
| amfi_code    | INTEGER   | Mutual fund identifier   |
| scheme_name  | TEXT      | Scheme name              |
| fund_house   | TEXT      | Asset management company |
| category     | TEXT      | Fund category            |
| sub_category | TEXT      | Fund sub-category        |

---

## Dimension Table: dim_date

| Column Name | Data Type | Description           |
| ----------- | --------- | --------------------- |
| date_id     | INTEGER   | Surrogate primary key |
| full_date   | DATE      | Calendar date         |
| day         | INTEGER   | Day number            |
| month       | INTEGER   | Month number          |
| quarter     | INTEGER   | Quarter number        |
| year        | INTEGER   | Year number           |
| day_name    | TEXT      | Weekday name          |

---

## Fact Table: fact_nav

| Column Name | Data Type | Description             |
| ----------- | --------- | ----------------------- |
| nav_id      | INTEGER   | Primary key             |
| fund_id     | INTEGER   | Foreign key to dim_fund |
| date_id     | INTEGER   | Foreign key to dim_date |
| nav         | REAL      | Net Asset Value         |

---

## Fact Table: fact_transactions

| Column Name      | Data Type | Description             |
| ---------------- | --------- | ----------------------- |
| transaction_id   | INTEGER   | Primary key             |
| fund_id          | INTEGER   | Foreign key to dim_fund |
| date_id          | INTEGER   | Foreign key to dim_date |
| investor_id      | INTEGER   | Investor identifier     |
| transaction_type | TEXT      | SIP/Lumpsum/Redemption  |
| amount           | REAL      | Transaction amount      |
| kyc_status       | TEXT      | KYC status              |

---

## Fact Table: fact_performance

| Column Name       | Data Type | Description             |
| ----------------- | --------- | ----------------------- |
| performance_id    | INTEGER   | Primary key             |
| fund_id           | INTEGER   | Foreign key to dim_fund |
| date_id           | INTEGER   | Foreign key to dim_date |
| one_year_return   | REAL      | 1-year return           |
| three_year_return | REAL      | 3-year return           |
| five_year_return  | REAL      | 5-year return           |
| expense_ratio     | REAL      | Expense ratio           |

---

## Fact Table: fact_aum

| Column Name | Data Type | Description                   |
| ----------- | --------- | ----------------------------- |
| aum_id      | INTEGER   | Primary key                   |
| fund_id     | INTEGER   | Foreign key to dim_fund       |
| date_id     | INTEGER   | Foreign key to dim_date       |
| aum_value   | REAL      | Assets Under Management (INR) |

---

# Data Quality Rules

1. AMFI codes must be unique within Fund Master.
2. NAV values must be greater than zero.
3. Transaction amounts must be greater than zero.
4. Expense ratio must be between 0.1% and 2.5%.
5. Dates must be stored in valid datetime format.
6. Duplicate records must be removed.
7. Transaction types must be standardized.
8. KYC status values must follow approved enums.

---

# Prepared By

Hema Mallipudi
B.Tech – Artificial Intelligence and Data Science
Mutual Fund Analytics Capstone Project
