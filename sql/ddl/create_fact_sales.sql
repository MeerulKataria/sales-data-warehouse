DROP TABLE IF EXISTS fact_sales CASCADE;

CREATE TABLE fact_sales (

    sale_key SERIAL PRIMARY KEY,

    customer_key INT NOT NULL,

    product_key INT NOT NULL,

    date_key INT NOT NULL,

    sales NUMERIC(10,2),

    quantity INT,

    discount NUMERIC(5,2),

    profit NUMERIC(10,2),

    CONSTRAINT fk_customer
        FOREIGN KEY (customer_key)
        REFERENCES dim_customer(customer_key),

    CONSTRAINT fk_product
        FOREIGN KEY (product_key)
        REFERENCES dim_product(product_key),

    CONSTRAINT fk_date
        FOREIGN KEY (date_key)
        REFERENCES dim_date(date_key)

);