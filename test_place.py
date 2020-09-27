from place import Place

def run_tests():
    """Test Place class."""
    print("Test empty places:")
    default_place = Place()
    print(default_place)
    assert default_place.city == ""
    assert default_place.priority == ""
    assert default_place.country == 0
    """Test initial places"""
    initial_place = Place("Rome", "Italy", 12,"n")
    print("Initial place:")
    print(initial_place)
    assert initial_place.city == "Rome"
    assert initial_place.country == "Italy"
    assert initial_place.priority == 12
    """Test mark method"""
    print("Mark the initial place as unvisited:")
    initial_place.mark_unvisited("n")
    print(initial_place)
    print("Mark the initial place as visited:")
    initial_place.mark_visited("v")
    print(initial_place)

run_tests()
