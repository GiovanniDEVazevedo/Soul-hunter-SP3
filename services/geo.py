import math


def distancia_haversine(lat1, lon1, lat2, lon2):
    raio_terra = 6371000.0

    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    dlat = lat1_rad - lat2_rad
    dlon = lon1_rad - lon2_rad

    a = math.sin(dlat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad)* math.sin(dlon / 2)** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a ))

    return raio_terra * c