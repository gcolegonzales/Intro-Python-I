# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class LatLong:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def __str__(self):
        return f"{self.lat}, {self.lon}"

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE

class Waypoint(LatLong):
    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)
        self.name = name

    def __str__(self):
        return f"{self.name}, is located at ({self.lat}, {self.lon})"

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE

class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        super().__init__(name, lat, lon)
        self.difficulty = difficulty
        self.size = size

    def __str__(self):
        return f"{self.name} - Difficulty: {self.difficulty} - Size: {self.size} - Coordinates: {self.lat}:{self.lon}"

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521
waypoint = Waypoint("Catacombs", 41.70505, -121.51521)
print(waypoint)

# YOUR CODE HERE

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556
newGeo = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)

# YOUR CODE HERE

# Print it--also make this print more nicely