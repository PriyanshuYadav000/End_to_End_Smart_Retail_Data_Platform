from datetime import datetime

def log_etl_run(
    pipeline_name,
    records_processed,
    status,
    error_message=None
):
    print("=" * 50)
    print(f"Pipeline: {pipeline_name}")
    print(f"Run Time: {datetime.now()}")
    print(f"Records Processed: {records_processed}")
    print(f"Status: {status}")

    if error_message:
        print(f"Error: {error_message}")

    print("=" * 50)