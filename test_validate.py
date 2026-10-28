
from extract import extract_data
from transform import transform_data
from validate import validate_data


def test_validate_data():
    df = extract_data()
    cleaned_df = transform_data(df)

    result = validate_data(cleaned_df)

    assert result is True
