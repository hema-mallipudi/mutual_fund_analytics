--1. Top 5 Funds by AUM
SELECT
    f.scheme_name,
    MAX(a.aum_value) AS max_aum
FROM fact_aum a
JOIN dim_fund f
ON a.fund_id = f.fund_id
GROUP BY f.scheme_name
ORDER BY max_aum DESC
LIMIT 5;
Insight

Finds the largest mutual funds by Assets Under Management.

--2. Average NAV Per Month
SELECT
    strftime('%Y-%m', d.full_date) AS month,
    ROUND(AVG(n.nav),2) AS avg_nav
FROM fact_nav n
JOIN dim_date d
ON n.date_id = d.date_id
GROUP BY month
ORDER BY month;
Insight

Shows NAV trends over time.

--3. SIP Year-over-Year Growth
SELECT
    strftime('%Y', d.full_date) AS year,
    SUM(t.amount) AS total_sip
FROM fact_transactions t
JOIN dim_date d
ON t.date_id = d.date_id
WHERE t.transaction_type = 'SIP'
GROUP BY year
ORDER BY year;
Insight

Measures SIP investment growth each year.

--4. Transactions by State

(If state exists in your transaction dataset)

SELECT
    state,
    COUNT(*) AS total_transactions,
    SUM(amount) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_amount DESC;
Insight

Identifies high-investment states.

--5. Funds with Expense Ratio < 1%
SELECT
    scheme_name,
    expense_ratio
FROM fact_performance fp
JOIN dim_fund f
ON fp.fund_id = f.fund_id
WHERE expense_ratio < 1
ORDER BY expense_ratio;
Insight

Finds low-cost mutual funds.

--6. Top 10 Funds by 5-Year Return
SELECT
    f.scheme_name,
    fp.five_year_return
FROM fact_performance fp
JOIN dim_fund f
ON fp.fund_id = f.fund_id
ORDER BY fp.five_year_return DESC
LIMIT 10;
Insight

Best long-term performers.

--7. Average Return by Fund Category
SELECT
    f.category,
    ROUND(AVG(fp.one_year_return),2) AS avg_return
FROM fact_performance fp
JOIN dim_fund f
ON fp.fund_id = f.fund_id
GROUP BY f.category
ORDER BY avg_return DESC;
Insight

Compares category performance.

--8. Total Transaction Amount by Type
SELECT
    transaction_type,
    COUNT(*) AS transactions,
    SUM(amount) AS total_amount
FROM fact_transactions
GROUP BY transaction_type;
Insight

Compares SIP, Lumpsum, and Redemption activity.

--9. Highest NAV Achieved by Each Fund
SELECT
    f.scheme_name,
    MAX(n.nav) AS highest_nav
FROM fact_nav n
JOIN dim_fund f
ON n.fund_id = f.fund_id
GROUP BY f.scheme_name
ORDER BY highest_nav DESC;
Insight

Shows peak NAV values.

--10. Funds by Risk Category
SELECT
    risk_category,
    COUNT(*) AS total_funds
FROM dim_fund
GROUP BY risk_category
ORDER BY total_funds DESC;
Insight

Distribution of funds by risk level.

Bonus Query (Interview Favorite)
Top 5 Fund Houses by Number of Schemes
SELECT
    fund_house,
    COUNT(*) AS total_schemes
FROM dim_fund
GROUP BY fund_house
ORDER BY total_schemes DESC
LIMIT 5;