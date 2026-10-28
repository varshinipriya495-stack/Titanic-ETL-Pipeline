
from extract import extract_data


def test_extract_data():
    df = extract_data()

    assert df is not None
    assert not df.empty
    assert len(df) == 891
    assert "survived" in df.columns
    assert "sex" in df.columns
