
def transform_data(df):
    print("Transforming Titanic dataset...", flush=True)

    # Keep only the required columns
    required_columns = [
        "survived",
        "pclass",
        "sex",
        "age",
        "sibsp",
        "parch",
        "fare",
        "embarked",
        "class",
        "who",
        "adult_male",
        "deck",
        "embark_town",
        "alive",
        "alone"
    ]

    df = df[required_columns].copy()

    # Check duplicate rows
    print("\nRows before removing duplicates:", len(df))

    duplicate_count = df.duplicated().sum()
    print("Duplicate rows found:", duplicate_count)

    # Remove duplicate rows
    df = df.drop_duplicates()

    print("Rows after removing duplicates:", len(df))

    # Fill missing values in age
    df["age"] = df["age"].fillna(df["age"].median())

    # Fill missing values in embarked
    df["embarked"] = df["embarked"].fillna(
        df["embarked"].mode()[0]
    )

    # Fill missing values in embark_town
    df["embark_town"] = df["embark_town"].fillna(
        df["embark_town"].mode()[0]
    )

    # Fill missing values in deck
    if "Unknown" not in df["deck"].cat.categories:
        df["deck"] = df["deck"].cat.add_categories(["Unknown"])

    df["deck"] = df["deck"].fillna("Unknown")

    # Display transformation results
    print("\nTransformation completed!")
    print("Rows and columns:", df.shape)

    print("\nMissing values after transformation:")
    print(df.isnull().sum())

    print("\nFirst 5 transformed rows:")
    print(df.head())

    return df
