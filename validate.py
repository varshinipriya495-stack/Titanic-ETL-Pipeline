
def validate_data(df):
    print("Validating Titanic dataset...", flush=True)

    if df is None or df.empty:
        print("Validation failed: Dataset is empty!")
        return False

    if df.isnull().sum().sum() > 0:
        print("Validation failed: Missing values found!")
        print(df.isnull().sum())
        return False

    if df.duplicated().any():
        print("Validation failed: Duplicate rows found!")
        return False

    print("Validation successful!")
    print("Rows:", df.shape[0])
    print("Columns:", df.shape[1])

    return True
