import re
locations_list = []
travel_points = 0
locations = input()
search_pattern = r"([=/])([A-Z][A-Za-z]{2}[A-Za-z]*)\1"
result = re.finditer(search_pattern, locations)
for match in result:
    locations_list.append(match.group(2))
for location in locations_list:
    travel_points += len(location)
print("Destinations: " + ", ".join(locations_list))
print(f"Travel Points: {travel_points}")