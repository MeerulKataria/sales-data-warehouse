DROP TABLE IF EXISTS dim_product CASCADE;

CREATE TABLE dim_product (

    product_key SERIAL PRIMARY KEY,

    product_id VARCHAR(20) UNIQUE,

    category VARCHAR(50),

    sub_category VARCHAR(50),

    product_name VARCHAR(200)

);