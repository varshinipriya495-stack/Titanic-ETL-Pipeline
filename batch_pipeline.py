
# batch_pipeline.py
"""Run the Titanic ETL pipeline in batches."""

import argparse

from extract import extract_data
from transform import transform_data
from validate import validate_data
from load import load_data


def run_batch_pipeline(batch_size=100, table_name="passengers"):

    if batch_size < 1:
        raise ValueError("Batch size must be at least 1")

    print("\n===== BATCH ETL PIPELINE STARTED =====")

    # Step 1: Extract
    raw = extract_data()

    if raw.empty:
        print("No rows found; nothing to load.")
        return

    print("Original rows:", len(raw))

    # Step 2: Remove duplicates across the entire dataset
    raw = raw.drop_duplicates().copy()

    print("Rows after removing duplicates:", len(raw))
    print("Batch size:", batch_size)

    total_rows = len(raw)
    loaded_rows = 0

    # Step 3: Process the deduplicated dataset in batches
    for batch_number, start in enumerate(
        range(0, total_rows, batch_size), start=1
    ):
        end = min(start + batch_size, total_rows)
        batch = raw.iloc[start:end].copy()

        print(
            f"\nProcessing batch {batch_number}: "
            f"rows {start + 1}-{end}"
        )

        # Transform
        clean_batch = transform_data(batch)

        # Validate
        validation_result = validate_data(clean_batch)

        if validation_result is False:
            raise ValueError(
                f"Validation failed for batch {batch_number}"
            )

        # Load: replace on first batch, append on later batches
        mode = "replace" if batch_number == 1 else "append"

        load_data(
            clean_batch,
            table_name=table_name,
            if_exists=mode
        )

        loaded_rows += len(clean_batch)

        print(f"Batch {batch_number} completed.")

    print("\n===== BATCH ETL PIPELINE FINISHED =====")
    print("Rows loaded:", loaded_rows)
    print("Table name:", table_name)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run Titanic ETL using batch processing."
    )

    parser.add_argument(
        "--batch-size",
        type=int,
        default=100,
        help="Number of rows per batch (default: 100)"
    )

    parser.add_argument(
        "--table",
        default="passengers",
        help="Destination MySQL table (default: passengers)"
    )

    args = parser.parse_args()

    run_batch_pipeline(
        batch_size=args.batch_size,
        table_name=args.table
    )
