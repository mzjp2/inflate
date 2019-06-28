import pytest

from inflate.inflate import _read_json_file, Inflate

read_json_file = _read_json_file

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
