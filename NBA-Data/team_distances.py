import csv
from math import radians, sin, cos, sqrt, atan2

def haversine_distance(lon1, lat1, lon2, lat2):
    # Convert latitude and longitude from degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    radius_earth = 6371  # Radius of the Earth in kilometers
    distance = radius_earth * c
    return distance

# Function to calculate distances between pairs of coordinates
def calculate_distances(locations):
    distances = {}
    for origin_name, origin_coord in locations.items():
        distances[origin_name] = {}
        for dest_name, dest_coord in locations.items():
            if origin_name != dest_name:
                distance = haversine_distance(*origin_coord, *dest_coord)
                distances[origin_name][dest_name] = distance
    return distances

# NBA team locations
nba_team_locations = {
    'Atlanta Hawks': [33.7573, -84.3963],
    'Boston Celtics': [42.3662, -71.0621],
    'Brooklyn Nets': [40.6826, -73.9745],
    'Charlotte Hornets': [35.2251, -80.8392],
    'Chicago Bulls': [41.8806, -87.6742],
    'Cleveland Cavaliers': [41.4966, -81.6881],
    'Dallas Mavericks': [32.7903, -96.8103],
    'Denver Nuggets': [39.7487, -105.0077],
    'Detroit Pistons': [42.3411, -83.0553],
    'Golden State Warriors': [37.7680, -122.3875],
    'Houston Rockets': [29.7508, -95.3621],
    'Indiana Pacers': [39.7639, -86.1555],
    'LA Clippers': [34.0430, -118.2673],
    'Los Angeles Lakers': [34.0430, -118.2673],
    'Memphis Grizzlies': [35.1380, -90.0504],
    'Miami Heat': [25.7814, -80.1866],
    'Milwaukee Bucks': [43.0436, -87.9169],
    'Minnesota Timberwolves': [44.9795, -93.2765],
    'New Orleans Pelicans': [29.9489, -90.0814],
    'New York Knicks': [40.7505, -73.9934],
    'Oklahoma City Thunder': [35.4634, -97.5151],
    'Orlando Magic': [28.5392, -81.3839],
    'Philadelphia 76ers': [39.9012, -75.1719],
    'Phoenix Suns': [33.4457, -112.0712],
    'Portland Trail Blazers': [45.5316, -122.6668],
    'Sacramento Kings': [38.5802, -121.4996],
    'San Antonio Spurs': [29.4271, -98.4375],
    'Toronto Raptors': [43.6435, -79.3791],
    'Utah Jazz': [40.7683, -111.9011],
    'Washington Wizards': [38.8981, -77.0209]
}


# Calculate distances
distances = calculate_distances(nba_team_locations)

for origin, dest_dict in distances.items():
    for dest, distance in dest_dict.items():
        distances[origin][dest] *= 0.621371

# Output CSV file
output_file = "nba_distances.csv"

# Write distances to CSV file
with open(output_file, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    # Write header row
    csvwriter.writerow(['Teams'] + list(nba_team_locations.keys()))
    for origin_team, origin_distances in distances.items():
        row = [origin_team]
        for dest_team in nba_team_locations.keys():
            if dest_team != origin_team:
                row.append(origin_distances[dest_team])
            else:
                row.append(0)  # Distance to itself is 0
        csvwriter.writerow(row)

print(f"Distances saved to {output_file}")