# osmtilecalc
Calculates Open Street Map tile coordinates required to map the given area
at certain zoom level.

Mapped area (bounding box) is a rectangle determined by given location coordinates and
the radius parameter in kilometers which is a distance from the location to the corners
of the rectangle.

Returns a list of urls pointing to calculated tiles.

# usage

main.py latitude longitude radius zoom_level [-h] [-t] [-m]

positional arguments:
  latitude          Latitude of location in decimal format
  longitude         Longitude of location in decimal format
  radius            Radius from location in kilometers
  zoom_level        Map zoom level (0-21)

optional arguments:
  -h, --help        show this help message and exit
  -t, --total-only  Only show total number of tiles
  -m, --miles       Change radius unit to US mile