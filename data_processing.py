import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


def filter_items(condition, dict_list):
    """Return a new list of dictionaries satisfying condition."""
    return [item for item in dict_list if condition(item)]


def aggregate(aggregation_key, aggregation_function, dict_list):
    """Apply an aggregation function to values from a dictionary key."""
    values = [item[aggregation_key] for item in dict_list]
    return aggregation_function(values)


cities = []
with open(os.path.join(__location__, 'Cities.csv'), encoding='utf-8-sig', newline='') as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

# Print first 5 cities only (as in the teacher's starter file)
for city in cities[:5]:
    print(city)

# Helper aggregation function: CSV values are strings, so convert to float
mean_temp = lambda values: sum(float(t) for t in values) / len(values)

# Print the average temperature of all the cities (first demonstration)
print("The average temperature of all the cities:")
print(aggregate('temperature', mean_temp, cities))
print()

# Print the average temperature of all the cities (second demonstration)
print("The average temperature of all the cities:")
print(aggregate('temperature', mean_temp, cities))
print()

# Print all cities in Germany
print("All cities in Germany:")
germany = filter_items(lambda city: city['country'] == 'Germany', cities)
for city in germany:
    print(city['city'])
print()

# Print all cities in Spain with a temperature above 12 C
print("Cities in Spain with temperature above 12 C:")
spain_above_12 = filter_items(
    lambda city: city['country'] == 'Spain' and float(city['temperature']) > 12,
    cities
)
for city in spain_above_12:
    print(city['city'], city['temperature'])
print()

# Count the number of unique countries
print("Number of unique countries:")
print(aggregate('country', lambda values: len(set(values)), cities))
print()

# Print the average temperature for all the cities in Germany
print("Average temperature of all cities in Germany:")
print(aggregate('temperature', mean_temp, germany))
print()

# Print the max temperature for all the cities in Italy
print("Maximum temperature of all cities in Italy:")
italy = filter_items(lambda city: city['country'] == 'Italy', cities)
print(aggregate('temperature', lambda values: max(float(t) for t in values), italy))
print()
