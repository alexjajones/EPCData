from src.data_utils import clean_data, get_epc_data


def test_clean_data():
    columns = ["LMK_KEY", "LODGEMENT_DATE", "TRANSACTION_TYPE", "TOTAL_FLOOR_AREA", "ADDRESS", "POSTCODE"]

    data = get_epc_data('test/test-data.zip', True)
    df = clean_data(data, columns)

    assert list(df.columns) == columns
