CREATE TABLE dim_customer (

    customer_key SERIAL PRIMARY KEY,

    customer_id VARCHAR(20) UNIQUE NOT NULL,

    customer_name VARCHAR(100) NOT NULL,

    segment VARCHAR(50),

    city VARCHAR(50),

    state VARCHAR(50),

    region VARCHAR(50)

);