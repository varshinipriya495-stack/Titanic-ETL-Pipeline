
from extract import extract_data
from transform import transform_data
from validate import validate_data
from load import load_data


def run_pipeline():
    print("\n===== TITANIC ETL PIPELINE STARTED =====\n")

    # Step 1: Extract
    df = extract_data()

    if df is None:
        print("Pipeline stopped: Extraction failed.")
        return
    # Step 2: Transform
    df = transform_data(df)

    # Step 3: Validate
    is_valid = validate_data(df)

    if not is_valid:
        print("Pipeline stopped: Validation failed.")
        return

    # Step 4: Load
    load_data(df)

    print("\n===== TITANIC ETL PIPELINE FINISHED =====")


if __name__ == "__main__":
    run_pipeline()
