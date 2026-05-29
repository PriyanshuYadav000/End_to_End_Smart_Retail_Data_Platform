CREATE TABLE etl_run_log (
    run_id INT AUTO_INCREMENT PRIMARY KEY,
    pipeline_name VARCHAR(100),
    start_time DATETIME,
    end_time DATETIME,
    records_processed INT,
    status VARCHAR(20),
    error_message VARCHAR(500)
);

INSERT INTO etl_run_log(
    pipeline_name,
    start_time,
    end_time,
    records_processed,
    status
)
VALUES(
    'Products_ETL',NOW(),NOW(),194,'SUCCESS'
);

INSERT INTO etl_run_log(
    pipeline_name,
    start_time,
    end_time,
    records_processed,
    status
)
VALUES(
    'Users_ETL',NOW(),NOW(),200,'SUCCESS'
);

INSERT INTO etl_run_log(
    pipeline_name,
    start_time,
    end_time,
    records_processed,
    status
)
VALUES(
    'Carts_ETL',NOW(),NOW(),200,'SUCCESS'
);

SELECT *
FROM etl_run_log;








