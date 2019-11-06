from tile_calculator.main import parse_args


def test_main():
    parser = parse_args(["54", "18", "1", "10"])
    assert parser.latitude == 54
    assert parser.longitude == 18
    assert parser.radius == 1
    assert parser.zoom_level == 10
    assert not parser.miles
    assert not parser.total_only
