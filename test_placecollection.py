from placecollection import PlaceCollection

def run_tests():
    """Test PlaceCollection class."""

    print("Test empty PlaceCollection:")
    place_collection = PlaceCollection()
    print(place_collection)
    assert not place_collection.place
    print(place_collection)
    print("Test loading place:")
    place_collection.load_places()
    print(place_collection)
    assert place_collection.places
    print("Test sorting - priority:")
    place_collection.sort("Priority")
    print(place_collection)
    print("Test sorting - country:")
    place_collection.sort("Country")
    print(place_collection)
    print("Test sorting - city:")
    movie_collection.sort("City")
    print(place_collection)
    place_collection.save_places()
    print("Test counting place:")
    print("No of visited place: ", place_collection.visited_places_count())
    print("No of unvisited place: ", place_collection.unvisited_places_count())

run_tests()
