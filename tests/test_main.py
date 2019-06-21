import pytest

from inflate.main import read_json_file, get_country_json, get_inflation_amount

UK_FILEPATH = "./inflate/data/uk_inflation.json"
US_FILEPATH = "./inflate/data/us_inflation.json"


def test_main_read_json_file_uk():
    uk_data = read_json_file(UK_FILEPATH)
    for key in uk_data:
        assert isinstance(key, int)
        assert "inflation" in uk_data[key]
        assert isinstance(uk_data[key]["inflation"], int)


def test_main_read_json_file_us():
    us_data = read_json_file(US_FILEPATH)
    for key in us_data:
        assert isinstance(key, int)
        assert "inflation" in us_data[key]
        assert isinstance(us_data[key]["inflation"], int)


def test_main_read_json_file_error():
    nonsense_filepath = "inflation/data/nonsense.json"
    with pytest.raises(FileNotFoundError, match="does not exist"):
        read_json_file(nonsense_filepath)


def test_main_get_country_json_uk():
    assert get_country_json("uk") == read_json_file(UK_FILEPATH)


def test_main_get_country_json_us():
    assert get_country_json("us") == read_json_file(US_FILEPATH)
