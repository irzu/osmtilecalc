import pytest
from tile_calculator.validators import valid_latitude, valid_longitude, valid_zoomlevel


def test_valid_latitude():
    assert valid_latitude(0) == 0
    assert valid_latitude(-90) == -90
    assert valid_latitude(90) == 90
    with pytest.raises(Exception):
        valid_latitude(-91)
    with pytest.raises(Exception):
        valid_latitude(91)
    with pytest.raises(Exception):
        valid_latitude("a")


def test_valid_longitude():
    assert valid_longitude(0) == 0
    assert valid_longitude(-180) == -180
    assert valid_longitude(180) == 180
    with pytest.raises(Exception):
        valid_longitude(-190)
    with pytest.raises(Exception):
        valid_longitude(190)
    with pytest.raises(Exception):
        valid_longitude("a")


def test_valid_zoomlevel():
    assert valid_zoomlevel(0) == 0
    assert valid_zoomlevel(21) == 21
    with pytest.raises(Exception):
        valid_zoomlevel(-1)
    with pytest.raises(Exception):
        valid_zoomlevel(22)
    with pytest.raises(Exception):
        valid_zoomlevel("a")
