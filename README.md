# osmtilecalc
Calculates Open Street Map tile coordinates required to map the given area
at certain zoom level.

Mapped area (bounding box) is a rectangle determined by given location coordinates and
the radius parameter in kilometers which is a distance from the location to the corners
of the rectangle.

Returns a list of urls pointing to calculated tiles.