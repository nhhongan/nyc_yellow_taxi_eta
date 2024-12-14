def get_zone_coordinates(zone_name):
    zone_to_coordinates = {
        'zone1': (34.0522, -118.2437),
        'zone2': (40.7128, -74.0060),
    }
    return zone_to_coordinates.get(zone_name, (None, None))