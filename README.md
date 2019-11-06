# osmtilecalc

## Open Street Map Tile Calculator

Calculates Open Street Map tile coordinates required to map the given area
at certain zoom level.

Mapped area (bounding box) is a rectangle determined by given location coordinates and
the radius parameter in kilometers which is a distance from the location to the corners
of the rectangle.

Returns a list of urls pointing to calculated tiles.

## Usage

`osm-tile-calc latitude longitude radius zoom_level [-h] [-t] [-m]`

positional arguments:

  `latitude`  Latitude of location in decimal format

  `longitude` Longitude of location in decimal format

  `radius` Radius from location in kilometers

  `zoom_level` Map zoom level (0-21)

optional arguments:

  `-h, --help` Show this help message and exit

  `-t, --total-only` Only show total number of tiles

  `-m, --miles` Change radius unit to US mile

### Example

```shell
$ osm-tile-calc 54.5189 18.5305 5 12
https://c.tile.openstreetmap.org/12/2257/1304.png
https://b.tile.openstreetmap.org/12/2257/1305.png
https://a.tile.openstreetmap.org/12/2258/1304.png
https://c.tile.openstreetmap.org/12/2258/1305.png
https://c.tile.openstreetmap.org/12/2259/1304.png
https://c.tile.openstreetmap.org/12/2259/1305.png
```
