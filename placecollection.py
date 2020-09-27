from place import Place
from operator import attrgetter

class PlaceCollection:

   def __init__(self):
        """Creating a list """
        self.places = []
   def __str__(self):
        """For testing test_place collection"""
        return str(self.places)
   def add_place(self, city, country=0, priority=""):
        """Adding a new place into the list"""
        self.places.append(Place(city, country, priority, "n"))
   def load_places(self):
        """Reading csv file"""
        file = open('places.csv', 'r')
        for place in file:
            place_attr = place.split(",")
            self.places.append(Place(place_attr[0], int(place_attr[1]), place_attr[2], place_attr[3].strip()))
        file.close()
   def save_places(self):
        """Saving places into csv file"""
        file = open('places.csv', 'w')
        for place in self.places:
            file.write(
                place.city + "," + str(place.country) + "," + place.priority + "," + place.status + "\n")
        file.close()
   def sort(self, sort_method):
        """Sorting in order, first is the key, then by city"""
        if sort_method == "priority":
            self.places.sort(key=attrgetter("priority", "city"))
        elif sort_method == "Title":
            self.places.sort(key=attrgetter("city"))
        elif sort_method == "Year":
            self.places.sort(key=attrgetter("country", "city"))
        else:
            self.places.sort(key=attrgetter("status", "city"))
   def unvisited_places_count(self):
        """Counting the number of unvisited places"""
        unvisited_places = 0
        for place in self.places:
            if place.status == 'n':
                unvisited_places += 1
        return unvisited_places
   def visited_places_count(self):
        """Counting the number of visited places"""
        visited_places = 0
        for place in self.places:
            if place.status == 'v':
                visited_places += 1
        return visited_places
   def select_place(self, city):
        for place in self.places:
            if place.city == city:
                return place
   pass
