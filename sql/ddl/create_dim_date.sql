DROP TABLE IF EXISTS dim_date CASCADE;

CREATE TABLE dim_date (

    date_key INT PRIMARY KEY,

    full_date DATE NOT NULL,

    day INT,

    month INT,

    month_name VARCHAR(20),

    quarter INT,

    year INT,

    weekday VARCHAR(20)

);