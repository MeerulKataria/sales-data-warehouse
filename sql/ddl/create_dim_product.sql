CREATE TABLE dim_product (

    product_key SERIAL PRIMARY KEY,

    product_id VARCHAR(30) UNIQUE NOT NULL,

    product_name VARCHAR(150) NOT NULL,

    category VARCHAR(50),

    sub_category VARCHAR(50)

);