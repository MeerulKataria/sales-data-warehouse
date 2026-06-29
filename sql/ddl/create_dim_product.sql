DROP TABLE IF EXISTS dim_product CASCADE;

CREATE TABLE dim_product (

    product_key SERIAL PRIMARY KEY,

    product_id VARCHAR(20) UNIQUE,

    product_name VARCHAR(255),

    category VARCHAR(50),

    sub_category VARCHAR(50)

);