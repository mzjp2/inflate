import pytest

from inflate.inflate import _read_json_file, Inflate

read_json_file = _read_json_file

UK_FILEPATH = "./inflate/data/uk_inflation.json"
US_FILEPATH = "./inflate/data/us_inflation.json"
EUR_FILEPATH = "./inflate/data/eur_inflation.json"


def test_main_read_json_file_uk():
    uk_data = read_json_file(UK_FILEPATH)
    for key in uk_data:
        assert isinstance(key, int)
        assert "inflation" in uk_data[key]
        assert isinstance(uk_data[key]["inflation"], float)


def test_main_read_json_file_us():
    us_data = read_json_file(US_FILEPATH)
    for key in us_data:
        assert isinstance(key, int)
        assert "inflation" in us_data[key]
        assert isinstance(us_data[key]["inflation"], float)


def test_main_read_json_file_eur():
    eur_data = read_json_file(EUR_FILEPATH)
    for key in eur_data:
        assert isinstance(key, int)
        assert "inflation" in eur_data[key]
        assert isinstance(eur_data[key]["inflation"], float)


def test_main_read_json_file_error():
    nonsense_filepath = "inflation/data/nonsense.json"
    with pytest.raises(FileNotFoundError, match="does not exist"):
        read_json_file(nonsense_filepath)


def test_start_year_below_1751_error():
    start_year = 1750
    with pytest.raises(
        ValueError,
        match="We only support starting years of 1751 or later. You inputted 1750",
    ):
        Inflate(start_year=start_year)


def test_end_year_above_2018_error():
    end_year = 2019
    with pytest.raises(
        ValueError,
        match="We only support ending years of 2018 or earlier. You inputted 2019",
    ):
        Inflate(start_year=2017, end_year=end_year)


def test_country_setter():
    assert Inflate(start_year=2017, end_year=2018, country="eur").country == "eur"
    assert Inflate(start_year=2017, end_year=2018, country="uk").country == "uk"
    inflate_client = Inflate(start_year=2017, end_year=2018, country="us")
    with pytest.raises(
        ValueError,
        match="We currently only have inflation data for the UK, US and the Eurozone",
    ):
        Inflate(start_year=2017, end_year=2018, country="a")
    with pytest.raises(
        ValueError,
        match="We currently only have inflation data for the UK, US and the Eurozone",
    ):
        inflate_client.country = "a"

