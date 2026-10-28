
from extract import extract_data
from transform import transform_data


def test_transform_data():
    df = extract_data()
    print("Rows before transformation:", len(df))

    cleaned_df = transform_data(df)
    print("Rows after transformation:", len(cleaned_df))

    assert cleaned_df is not None
    assert not cleaned_df.empty
    assert cleaned_df.isnull().sum().sum() == 0
    assert len(cleaned_df.columns) == 15
