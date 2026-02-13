-- Total sales
SELECT SUM(amount) as total_sales FROM sales;

-- Average sales by category
SELECT category, AVG(amount) as avg_sales FROM sales GROUP BY category;

-- High-value sales
SELECT * FROM sales WHERE amount > 1000;
