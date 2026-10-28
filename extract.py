
import pandas as pd
import seaborn as sns


def extract_data():
    print("Extracting Titanic dataset...", flush=True)

    try:
        df = sns.load_dataset("titanic")

        print("Dataset extracted successfully!")
        print("Number of rows:", df.shape[0])
        print("Number of columns:", df.shape[1])
        print("\nFirst 5 rows:")
        print(df.head())

        return df

    except Exception as error:
        print("Dataset extraction failed:", error)
        return None


if __name__ == "__main__":
    extract_data()
