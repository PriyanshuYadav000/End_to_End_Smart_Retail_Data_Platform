-- Top 10 Most Expensive Products

SELECT
    title,
    category,
    price
FROM dim_products
ORDER BY price DESC
LIMIT 10;

-- Average Rating by Category

SELECT
    category,
    ROUND(AVG(rating),2) AS avg_rating
FROM dim_products
GROUP BY category
ORDER BY avg_rating DESC;

-- Products by Category

SELECT
    category,
    COUNT(*) AS total_products
FROM dim_products
GROUP BY category
ORDER BY total_products DESC;

-- Low Stock Products

SELECT
    product_id,
    title,
    stock
FROM dim_products
WHERE stock < 20
ORDER BY stock;

-- Revenue Analysis

SELECT
    ROUND(SUM(total),2) AS total_revenue,
    ROUND(AVG(total),2) AS average_cart_value,
    MAX(total) AS highest_cart_value
FROM fact_carts;

-- Top 10 Highest Value Carts

SELECT
    cart_id,
    user_id,
    total
FROM fact_carts
ORDER BY total DESC
LIMIT 10;

-- User Demographics

SELECT
    gender,
    COUNT(*) AS total_users
FROM dim_users
GROUP BY gender;

