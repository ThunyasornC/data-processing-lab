import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv'), encoding='utf-8-sig', newline='') as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

# Print first 5 cities only
for city in cities[:5]:
    print(city)

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = []
for city in cities:
    temps.append(float(city['temperature']))
print(sum(temps)/len(temps))
print()

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = [float(city['temperature']) for city in cities]
print(sum(temps)/len(temps))
print()

# Print all cities in Germany

print("All cities in Germany:")
germany = [city for city in cities if city['country'] == 'Germany']
for city in germany:
    print(city['city'])
print()

# Print all cities in Spain with a temperature above 12°C

print("Cities in Spain with temperature above 12 C:")
spain_above_12 = [
    city for city in cities
    if city['country'] == 'Spain' and float(city['temperature']) > 12
]
for city in spain_above_12:
    print(city['city'], city['temperature'])
print()

# Count the number of unique countries

print("Number of unique countries:")
countries = {city['country'] for city in cities}
print(len(countries))
print()

# Print the average temperature for all the cities in Germany

print("Average temperature of all cities in Germany:")
germany_temps = [float(city['temperature']) for city in germany]
print(sum(germany_temps) / len(germany_temps))
print()

# Print the max temperature for all the cities in Italy

print("Maximum temperature of all cities in Italy:")
italy_temps = [float(city['temperature']) for city in cities if city['country'] == 'Italy']
print(max(italy_temps))
print()
