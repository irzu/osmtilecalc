import pytest
from osmtilecalc.calculators import (
    tile_to_url,
    get_bounding_box,
    get_tile_coords,
    coordinates_to_tile_points,
    get_urls_for_location,
)


def test_tile_to_url():
    assert tile_to_url(54, 18, 10).endswith("tile.openstreetmap.org/10/54/18.png")


def test_get_bounding_box():
    bounding_box = get_bounding_box([54, 18], 1)
    lat_min, lat_max, lon_min, lon_max = bounding_box.values()
    assert lat_min == 53.990990990990994
    assert lat_max == 54.009009009009006
    assert lon_min == 17.984672958408073
    assert lon_max == 18.015327041591927


def test_get_bounding_box_invalid_args():
    with pytest.raises(Exception):
        get_bounding_box("a", "b")


def test_get_tile_coords():
    bounding_box = get_bounding_box([54, 18], 1)
    tile_coords_level_10 = get_tile_coords(bounding_box, 10)
    tile_coords_level_15 = get_tile_coords(bounding_box, 15)
    tile_coords_level_20 = get_tile_coords(bounding_box, 20)
    assert len(tile_coords_level_10) == 1
    assert len(tile_coords_level_15) == 12
    assert len(tile_coords_level_20) == 8190


def test_get_tile_coords_invalid_args():
    with pytest.raises(Exception):
        get_tile_coords("a", "b")


def test_coordinates_to_tile_points():
    bounding_box = get_bounding_box([54, 18], 1)
    tx_min, tx_max, ty_min, ty_max = coordinates_to_tile_points(
        bounding_box, 10
    ).values()
    assert tx_min == 563
    assert tx_max == 563
    assert ty_min == 328
    assert ty_max == 328


def test_coordinates_to_tile_points_invalid_args():
    with pytest.raises(Exception):
        coordinates_to_tile_points("a", "b")


def test_get_urls_for_location():
    urls_for_level_10 = get_urls_for_location([54, 18], 1, 10)
    urls_for_level_15 = get_urls_for_location([54, 18], 1, 15)
    urls_for_level_20 = get_urls_for_location([54, 18], 1, 20)
    assert len(urls_for_level_10) == 1
    assert len(urls_for_level_15) == 12
    assert len(urls_for_level_20) == 8190


def test_get_urls_for_location_invalid_args():
    with pytest.raises(Exception):
        get_urls_for_location("a", "b", "c")
