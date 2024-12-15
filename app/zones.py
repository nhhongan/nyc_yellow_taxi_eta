import pandas as pd
import os
from shapely import wkt
from shapely.geometry import Point

class TaxiZoneFinder:
    def __init__(self, csv_path):
        if not os.path.isabs(csv_path):
            current_dir = os.path.dirname(os.path.abspath(__file__))
            csv_path = os.path.join(current_dir, csv_path)
        self.zones_df = pd.read_csv(csv_path)
        self.zones_df['geometry'] = self.zones_df['zone_geom'].apply(wkt.loads)

    def get_zone_id(self, lat: float, lng: float) -> dict:
        """
        Get taxi zone ID for a given latitude and longitude
        Args:
            lat (float): Latitude
            lng (float): Longitude
        Returns:
            dict: Dictionary containing zone information or None if not found
        """
        try:
            point = Point(lng, lat) 

            for _, row in self.zones_df.iterrows():
                if row['geometry'].contains(point):
                    return {
                        'zone_id': row['zone_id'],
                        'borough': row['borough'],
                        'zone_name': row['zone_name']
                    }
            return None

        except Exception as e:
            print(f"Error finding zone: {str(e)}")
            return None

def main():
    taxi_zone_data_path = "../data/taxi_zone_lookup.csv"
    finder = TaxiZoneFinder(taxi_zone_data_path)
    
    # Test single coordinate
    lat, lng = 40.67467971441616, -73.74398274832727
    result = finder.get_zone_id(lat, lng)
    
    if result:
        print(f"Coordinates ({lat}, {lng}) are in:")
        print(f"Zone ID: {result['zone_id']}")
        print(f"Borough: {result['borough']}")
        print(f"Zone Name: {result['zone_name']}")
    else:
        print(f"No zone found for coordinates ({lat}, {lng})")

if __name__ == "__main__":
    main()