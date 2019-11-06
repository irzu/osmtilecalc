import math
import random


def coordinates_to_tile_points(bounding_box, zoom_level):
    """
    Converts given lat/lon bounds to tile points for given zoom level.
    """

    def lon_to_x(lon):
        """
        Converts longitude to x-axis points.
        """
        return math.floor((lon + 180) / 360 * math.pow(2, zoom_level))

    def lat_to_y(lat):
        """
        Converts latitude to y-axis points.
        """
        return math.floor(
            (
                1
                - math.log(
                    math.tan(lat * math.pi / 180) + 1 / math.cos(lat * math.pi / 180)
                )
                / math.pi
            )
            / 2
            * math.pow(2, zoom_level)
        )

    return {
        "tx_min": lon_to_x(bounding_box["lon_min"]),
        "tx_max": lon_to_x(bounding_box["lon_max"]),
        "ty_min": lat_to_y(bounding_box["lat_max"]),
        "ty_max": lat_to_y(bounding_box["lat_min"]),
    }


def get_bounding_box(location, radius):
    """
    Based on given location coordinates and radius in kilometers
    returns coordinates of the bounding box.
    """
    equator_len = 111
    current_latitude_km_length = math.cos(location[0] * math.pi / 180) * equator_len

    return {
        "lat_min": location[0] - radius / equator_len,
        "lat_max": location[0] + radius / equator_len,
        "lon_min": location[1] - radius / current_latitude_km_length,
        "lon_max": location[1] + radius / current_latitude_km_length,
    }


def tile_to_url(tile_x, tile_y, tile_z):
    """
    Generates url with given x,y,z params.
    """
    subdomain = random.choice(["a", "b", "c"])
    resource_url = "https://{0}.tile.openstreetmap.org/{1}/{2}/{3}.png"
    return resource_url.format(subdomain, tile_z, tile_x, tile_y)


def get_tile_coords(bounding_box, zoom_level):
    """
    Iterates over the bounding box and converts coordinates to points
    returning dictionaries with x,y,z params for each tile.
    """
    tile_bounds = []
    tile_points = coordinates_to_tile_points(bounding_box, zoom_level)
    tx_min, tx_max, ty_min, ty_max = tile_points.values()
    tile_x = tx_min
    while tile_x <= tx_max:
        tile_y = ty_min
        while tile_y <= ty_max:
            tile_bounds.append(
                {"tile_x": tile_x, "tile_y": tile_y, "tile_z": zoom_level}
            )
            tile_y += 1
        tile_x += 1
    return tile_bounds


def get_urls_for_location(location, radius, zoom_level):
    """
    Based on given coordinates and radius expressed in kilometers
    returns an array of tile urls covering the area at given zoom level.
    """
    tile_urls = []
    bounding_box = get_bounding_box(location, radius)
    tile_coords = get_tile_coords(bounding_box, zoom_level)

    for tile in tile_coords:
        tile_urls.append(tile_to_url(tile["tile_x"], tile["tile_y"], tile["tile_z"]))

    return tile_urls
