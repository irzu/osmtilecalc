#!/usr/bin/env python
"""
Calculates Open Street Map tile coordinates required to map the given area
at certain zoom level.

Mapped area (bounding box) is a rectangle determined by given location coordinates and
the radius parameter in kilometers which is a distance from the location to the corners
of the rectangle.

Returns a list of urls pointing to calculated tiles and number of required tiles.
"""
import argparse
import pprint
import sys
from tile_calculator.calculators import get_urls_for_location
from tile_calculator.validators import valid_latitude, valid_longitude, valid_zoomlevel


def parse_args(args):
    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument(
        "latitude", 
        type=valid_latitude, 
        help="Latitude of location in decimal format",
    )

    parser.add_argument(
        "longitude",
        type=valid_longitude,
        help="Longitude of location in decimal format",
    )

    parser.add_argument(
        "radius", 
        type=int, 
        help="Radius from location in kilometers"
    )

    parser.add_argument(
        "zoom_level", 
        type=valid_zoomlevel, 
        help="Map zoom level (0-21)"
    )

    parser.add_argument(
        "-t", "--total-only",
        action="store_true",
        help="Only show total number of tiles",
    )

    parser.add_argument(
        "-m", "--miles", 
        action="store_true", 
        help="Change radius unit to US mile"
    )

    return parser.parse_args(args)


def main():
    args = parse_args(sys.argv[1:])
    radius = args.radius if not args.miles else args.radius * 1.60934
    tiles = get_urls_for_location(
        [args.latitude, args.longitude], radius, args.zoom_level
    )
    if args.total_only:
        print("Total tiles:", len(tiles))
    else:
        pprint.pprint(tiles)


if __name__ == "__main__":
    main()
