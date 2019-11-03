import math
import random
import argparse

PARSER = argparse.ArgumentParser(description="Calculate osm tiles.")

PARSER.add_argument(
    "latitude",
    metavar="lat",
    type=int,
    nargs=1,
    help="Latitude (in decimal format)",
)

PARSER.add_argument(
    "longitude",
    metavar="lon",
    type=int,
    nargs=1,
    help="Longitude (in decimal format)",
)

PARSER.add_argument(
    "radius",
    metavar="radius",
    type=int,
    nargs=1,
    default=1,
    help="Radius in kilometers",
)

PARSER.add_argument(
    "minzoom",
    metavar="minzoom",
    type=int,
    nargs=1,
    default=1,
    choices=range(0, 21),
    help="Zoom level between 0 and 20",
)

PARSER.add_argument(
    "maxzoom",
    metavar="maxzoom",
    type=int,
    nargs=1,
    default=1,
    choices=range(0, 21),
    help="Zoom level between 0 and 20",
)

ARGS = PARSER.parse_args()


def calculate_bounds(lat_min, lat_max, lon_min, lon_max, zoom):
    def lon_to_tile_x(lon, zoom):
        return math.floor((lon + 180) / 360 * math.pow(2, zoom))

    def lat_to_tile_y(lat, zoom):
        return math.floor(
            (
                1
                - math.log(
                    math.tan(lat * math.pi / 180)
                    + 1 / math.cos(lat * math.pi / 180)
                )
                / math.pi
            )
            / 2
            * math.pow(2, zoom)
        )

    bounds = {
        "tx_min": lon_to_tile_x(lon_min, zoom),
        "tx_max": lon_to_tile_x(lon_max, zoom),
        "ty_min": lat_to_tile_y(lat_max, zoom),
        "ty_max": lat_to_tile_y(lat_min, zoom),
    }

    return bounds


def get_lat_lon_range(lat, lon, radius):
    equator_len = 111
    current_latitude_km_length = math.cos(lat * math.pi / 180) * equator_len
    lat_min = lat - radius / equator_len
    lat_max = lat + radius / equator_len
    lon_min = lon - radius / current_latitude_km_length
    lon_max = lon + radius / current_latitude_km_length
    return {
        "lat_min": lat_min,
        "lat_max": lat_max,
        "lon_min": lon_min,
        "lon_max": lon_max,
    }


def tile_to_url(x, y, z):
    subdomain = random.choice(["a", "b", "c"])
    resource_url = "https://{0}.tile.openstreetmap.org/{1}/{2}/{3}.png"
    return resource_url.format(subdomain, z, x, y)


def get_tile_coords(lat_min, lat_max, lon_min, lon_max, zoomMin, zoomMax):
    tileBounds = []
    zoom = zoomMin
    while zoom <= zoomMax:
        bounds = calculate_bounds(lat_min, lat_max, lon_min, lon_max, zoom)
        tx_min = bounds["tx_min"]
        tx_max = bounds["tx_max"]
        ty_min = bounds["ty_min"]
        ty_max = bounds["ty_max"]
        tile_x = tx_min
        while tile_x <= tx_max:
            tile_y = ty_min
            while tile_y <= ty_max:
                tileBounds.append(
                    {"tile_x": tile_x, "tile_y": tile_y, "tile_z": zoom}
                )
                tile_y += 1
            tile_x += 1
        zoom += 1
    return tileBounds


def get_urls_for_location(lat, lon, radius, zoomMin, zoomMax):
    tileUrls = []
    lat_lon_range = get_lat_lon_range(lat, lon, radius)
    tileCoords = get_tile_coords(
        lat_lon_range["lat_min"],
        lat_lon_range["lat_max"],
        lat_lon_range["lon_min"],
        lat_lon_range["lon_max"],
        zoomMin,
        zoomMax,
    )
    for tile in tileCoords:
        tileUrls.append(tile_to_url(tile["x"], tile["y"], tile["z"]))

    return tileUrls


def main(location, radius, zoom_range):
    get_urls_for_location(
        location[0], location[1], radius, zoom_range[0], zoom_range[1]
    )
