import sys
from tile_calculator.main import main, parse_args


def test_parse_args():
    parser = parse_args(["54", "18", "1", "10"])
    assert parser.latitude == 54
    assert parser.longitude == 18
    assert parser.radius == 1
    assert parser.zoom_level == 10
    assert not parser.miles
    assert not parser.total_only


def test_main(capsys):
    sys.argv[1:5] = ["54", "18", "1", "10"]
    main()
    captured = capsys.readouterr()
    assert captured.out.endswith("tile.openstreetmap.org/10/563/328.png\n")


def test_main_with_t_param(capsys):
    sys.argv[1:5] = ["54", "18", "1", "10", "-t"]
    main()
    captured = capsys.readouterr()
    assert captured.out == "Total tiles: 1\n"
