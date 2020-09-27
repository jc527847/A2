class Place:
    """Class with the required attributes for a place"""

    def __init__(self, city="", country=0, priority="", status=""):
        """Defining the place object"""
        self.city = city
        self.country = country
        self.priority = priority
        self.status = status

    def __str__(self):
        """Display details"""
        return "{} ({} from {}) {}".format(self.city, self.priority, self.country, self.status)

    __repr__ = __str__

    def mark_visited(self, status):
        """Mark the place"""
        if status == "n":
            self.status = "v"
            return True
        elif status == "v":
            return False

    def mark_unvisited(self, status):
        """Mark the place as unvisited"""
        if status == "v":
            self.status = "n"
            return True
        elif status == "n":
            return False

    pass
