
-- MUTUAL FUND ANALYTICS STAR SCHEMA

-- DIMENSION TABLE: FUND


CREATE TABLE dim_fund (
fund_id INTEGER PRIMARY KEY AUTOINCREMENT,
amfi_code INTEGER UNIQUE NOT NULL,
scheme_name TEXT NOT NULL,
fund_house TEXT,
category TEXT,
sub_category TEXT,
plan TEXT,
fund_manager TEXT,
risk_category TEXT
);

-- DIMENSION TABLE: DATE

CREATE TABLE dim_date (
date_id INTEGER PRIMARY KEY AUTOINCREMENT,
full_date DATE UNIQUE NOT NULL,
day INTEGER,
month INTEGER,
quarter INTEGER,
year INTEGER,
day_name TEXT
);

-- FACT TABLE: NAV HISTORY

CREATE TABLE fact_nav (
nav_id INTEGER PRIMARY KEY AUTOINCREMENT,

```
fund_id INTEGER NOT NULL,
date_id INTEGER NOT NULL,

nav REAL NOT NULL,

FOREIGN KEY (fund_id)
    REFERENCES dim_fund(fund_id),

FOREIGN KEY (date_id)
    REFERENCES dim_date(date_id)
```

);

-- FACT TABLE: INVESTOR TRANSACTIONS


CREATE TABLE fact_transactions (
transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,

```
fund_id INTEGER NOT NULL,
date_id INTEGER NOT NULL,

investor_id INTEGER,

transaction_type TEXT,
amount REAL NOT NULL,
kyc_status TEXT,

FOREIGN KEY (fund_id)
    REFERENCES dim_fund(fund_id),

FOREIGN KEY (date_id)
    REFERENCES dim_date(date_id)
```

);


-- FACT TABLE: SCHEME PERFORMANCE


CREATE TABLE fact_performance (
performance_id INTEGER PRIMARY KEY AUTOINCREMENT,

```
fund_id INTEGER NOT NULL,
date_id INTEGER NOT NULL,

one_year_return REAL,
three_year_return REAL,
five_year_return REAL,

expense_ratio REAL,

FOREIGN KEY (fund_id)
    REFERENCES dim_fund(fund_id),

FOREIGN KEY (date_id)
    REFERENCES dim_date(date_id)
```

);


-- FACT TABLE: AUM


CREATE TABLE fact_aum (
aum_id INTEGER PRIMARY KEY AUTOINCREMENT,

```
fund_id INTEGER NOT NULL,
date_id INTEGER NOT NULL,

aum_value REAL NOT NULL,

FOREIGN KEY (fund_id)
    REFERENCES dim_fund(fund_id),

FOREIGN KEY (date_id)
    REFERENCES dim_date(date_id)
```

);
