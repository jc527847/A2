from placecollection import PlaceCollection

MENU_STRING = "\nL - List places\nA - Add new place\nM - Mark a place as visited\nQ - Quit\n"
place_collection = PlaceCollection()


def main():
    place_collection.load_places()
    print("Places To Visit 1.0 - by <Chen chen>")
    menu()


def place_list():
    """Shows the place list"""
    count = 1
    for place in place_collection.places:
        if place.status == "u":
            print("{}.* {}".format(count, place))
        else:
            print("{}. {}".format(count, place))
        count += 1
    print('{} places visited, {} places still to visit'.format(place_collection.visited_places_count(),
                                                               place_collection.unvisited_places_count()))

def visit_place():

    total = place_collection.visited_places_count() + place_collection.unvisited_places_count()

    print("Enter the number of a place to mark as visited")
    """Error checking"""
    finished = False
    while not finished:
        try:
            choice = int(input(">>> "))
            if 0 < choice <= total:
                # check if the place is visited
                if place_collection.select_place(choice).status == "v":
                    print("You have already visited")
                else:
                    print("{} from {} visited".format(place_collection.select_place(choice).city,
                                                      place_collection.select_place(choice).country))
                    place_collection.select_place(choice).status = "v"
                finished = True
            elif choice >= total:
                print("Invalid place number")
            else:
                print("Number must be > 0")
        except ValueError:
            print("Invalid input; enter a valid number")

def add_place():
    city = input("city:")
    while not title.strip():
        print("Input can not be blank")
        city = input("City:")

    country = ""
    finished = False
    while not finished:
        try:
            country = int(input("Country:"))
            if country >= 0:
                finished = True
            else:
                print("Number must be >= 0")
        except ValueError:
            print("Invalid input; enter a valid number")

    priority = input("Priority:")
    while not priority.strip():
        print("Input can not be blank")
        priority = input("Priority:")

    print("{} ({} from {}) added to place list".format(city, country, priority))

def menu():
    print("Menu:")
    print(MENU_STRING)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "L":
            movie_list()
        elif choice == "A":
            add_movie()
        elif choice == "M":
            visit_place(choice)
        else:
            print("Invalid choice")

        print("Menu:")
        print(MENU_STRING)
        choice = input(">>> ").upper()

    print("{} places saved to place.csv".format(
        place_collection.unvisited_places_count() + place_collection.watched_places_count()))
    print("Have a good time")

if __name__ == '__main__':
    main()
