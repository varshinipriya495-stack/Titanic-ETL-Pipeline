
# Titanic ETL Pipeline

## Project Overview

An ETL (Extract, Transform, Load) pipeline built using Python, Pandas, and MySQL to extract, clean, validate, and load Titanic dataset records.

## Technologies Used

- Python
- Pandas
- MySQL
- SQLAlchemy
- Pytest

## ETL Process

1. **Extract:** Read the Titanic dataset.
2. **Transform:** Remove duplicate rows and handle missing values.
3. **Validate:** Check the cleaned data.
4. **Load:** Store the processed data in MySQL.

## Batch Processing

The project supports batch processing and loading.

Run the batch pipeline:

```bash
python batch_pipeline.py
```

Run with a batch size of 100:

```bash
python batch_pipeline.py --batch-size 100
```

## Run the Normal Pipeline

```bash
python pipeline.py
```

## Run Automated Tests

```bash
pytest -v
```

## Results

- Original dataset: 891 rows
- Rows after duplicate removal: 784
- Number of columns: 15
- Automated tests: 4 passed

## Project Files

- `extract.py` — Extracts the Titanic dataset.
- `transform.py` — Cleans and transforms the data.
- `validate.py` — Validates the dataset.
- `load.py` — Loads data into MySQL.
- `pipeline.py` — Runs the normal ETL pipeline.
- `batch_pipeline.py` — Runs the batch pipeline.
- `test_connection.py` — Tests the MySQL connection.
- `test_extract.py` — Tests data extraction.
- `test_transform.py` — Tests data transformation.
- `test_validate.py` — Tests data validation.

## Conclusion

This project demonstrates ETL pipeline development, data cleaning, MySQL integration, batch processing, and automated testing.
