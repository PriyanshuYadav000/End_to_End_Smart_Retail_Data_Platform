
-- 1. Product Record Count Validation

SELECT COUNT(*) AS total_products
FROM dim_products;

-- 2. User Record Count Validation

SELECT COUNT(*) AS total_users
FROM dim_users;

-- 3. Cart Record Count Validation

SELECT COUNT(*) AS total_carts
FROM fact_carts;


-- 4. Duplicate Product IDs

SELECT product_id, COUNT(*)
FROM dim_products
GROUP BY product_id
HAVING COUNT(*) > 1;

-- 5. Duplicate User IDs

SELECT user_id, COUNT(*)
FROM dim_users
GROUP BY user_id
HAVING COUNT(*) > 1;

-- 6. Duplicate Cart IDs

SELECT cart_id, COUNT(*)
FROM fact_carts
GROUP BY cart_id
HAVING COUNT(*) > 1;


-- 7. Null Product Titles

SELECT *
FROM dim_products
WHERE title IS NULL;

-- 8. Null User Names

SELECT *
FROM dim_users
WHERE full_name IS NULL;

-- 9. Null Cart Totals

SELECT *
FROM fact_carts
WHERE total IS NULL;

-- BUSINESS VALIDATION CHECKS

-- 10. Products Per Category

SELECT
    category,
    COUNT(*) AS total_products
FROM dim_products
GROUP BY category
ORDER BY total_products DESC;

-- 11. User Gender Distribution

SELECT
    gender,
    COUNT(*) AS total_users
FROM dim_users
GROUP BY gender;

-- 12. Revenue Validation

SELECT
    ROUND(SUM(total),2) AS total_revenue
FROM fact_carts;