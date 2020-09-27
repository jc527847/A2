"""
Name: Chen chen
Date: 27/09/2020
Brief Project Description: A project with GUI and Console programs that use classes to manage a list of Movies to Watch.
GitHub URL: https://github.com/JCUS-CP1404/assignment-2-travel-tracker-jc527847
"""
from placecollection import PlaceCollection
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.lang import Builder


class PlacesToVisitApp(App):
    """Main program"""

    def __init__(self, **kwargs):
        """Variables for Place and PlaceCollection class"""
        super().__init__(**kwargs)
        self.place_list = PlaceCollection()
        """MovieCollection class"""
        self.top_label = Label(text="", id="count_label")
        self.sort_label = Label(text="Sort by:")
        self.spinner = Spinner(text='Priority', values=('Priority', 'City', 'Country', 'Visited'))
        self.add_place_label = Label(text="Add New Place...")
        self.city_label = Label(text="City:")
        self.city_text_input = TextInput(write_tab=False, multiline=False)
        self.priority_label = Label(text="Priority:")
        self.priority_text_input = TextInput(write_tab=False, multiline=False)
        self.country_label = Label(text="Country:")
        self.country_text_input = TextInput(write_tab=False, multiline=False)

        self.add_place_button = Button(text='Add Place')
        """Button of adding places"""
        self.clear_button = Button(text='Clear')
        """Button of clearing all the text"""

    def build(self):
        """Creating basic component"""
        self.city = "Places to Visit 2.0"
        self.root = Builder.load_file('app.kv')
        self.place_list.load_places()
        """Asking the load_places method to load csv file"""
        self.place_list.sort('Priority')
        """Ordering the list by category"""
        """Divide layouts into two parts"""
        self.build_left_widgets()
        self.build_right_widgets()
        return self.root

    def build_left_widgets(self):
        """Creating the left widget"""
        self.root.ids.topLayout.add_widget(self.top_label)
        self.root.ids.leftLayout.add_widget(self.sort_label)
        self.root.ids.leftLayout.add_widget(self.spinner)
        self.root.ids.leftLayout.add_widget(self.add_place_label)
        self.root.ids.leftLayout.add_widget(self.city_label)
        self.root.ids.leftLayout.add_widget(self.city_text_input)
        self.root.ids.leftLayout.add_widget(self.priorityy_label)
        self.root.ids.leftLayout.add_widget(self.priority_text_input)
        self.root.ids.leftLayout.add_widget(self.country_label)
        self.root.ids.leftLayout.add_widget(self.country_text_input)
        self.root.ids.leftLayout.add_widget(self.add_place_button)
        self.root.ids.leftLayout.add_widget(self.clear_button)
        """Adding effects for buttons"""
        self.spinner.bind(text=self.sorting_places)
        """Sorting in order, first is the key, then by city"""
        self.clear_button.bind(on_release=self.clear_text)
        """Clearing all text"""
        self.add_movie_button.bind(on_release=self.error_checking)

    def build_right_widgets(self):
        """Building the right widget"""
        self.top_label.text = "To visit: " + str(self.place_list.unvisited_places_count()) + ". Visited: " + \
                              str(self.place_list.visited_places_count())
        """Shows the number of visited and unvisited places"""

        for place in self.place_list.places:
            if place.status == 'v':
                place_button = Button(text="{} ({} from {}) visited".
                                      format(place.city, place.priority, place.country), id=place.city)
                place_button.background_color = [90, 90, 0, 0.5]
                """Managing the background color"""
            else:
                place_button = Button(text="{} ({} from {})".
                                      format(place.city, place.priority, place.country), id=place.city)
                place_button.background_color = [0, 90, 90, 0.5]

            place_button.bind(on_release=self.visit_place)
            self.root.ids.rightLayout.add_widget(place_button)

    def visit_place(self, button):

        if self.place_list.select_place(button.id).status == 'n':
            self.place_list.select_place(button.id).status = 'v'
            self.root.ids.bottomLayout.text = "You have visited " + str(self.place_list.select_place(button.id).city)
        else:
            self.place_list.select_place(button.id).status = 'n'
            self.root.ids.bottomLayout.text = "You need to visit " + str(self.place_list.select_place(button.id).city)
        """Ordering the list again with each select"""
        self.sorting_places()
        self.root.ids.rightLayout.clear_widgets()
        self.build_right_widgets()

    def sorting_places(self, *args):
        """Sorting movies eith the sort method """
        self.place_list.sort(self.spinner.text)
        self.root.ids.rightLayout.clear_widgets()
        self.build_right_widgets()

    def clear_text(self, *args):
        """Clearing all text"""
        self.city_text_input.text = ""
        self.priority_text_input.text = ""
        self.country_text_input.text = ""
        self.root.ids.bottomLayout.text = ""

    def error_checking(self, *args):
        """Error checking"""

        if str(self.city_text_input.text).strip() == '' or str(self.priority_text_input.text).strip() == '' \
                or str(self.country_text_input.text).strip() == '':
            self.root.ids.bottomLayout.text = "All fields must be completed"

        elif self.priority_text_input.text != "1" and self.priority_text_input.text != "2" \
                and self.category_text_input.text != "3" and self.category_text_input.text != "4" \
                and self.category_text_input.text != "5" and self.category_text_input.text != "6":
            self.root.ids.bottomLayout.text = \
                "Priority must be one of 1, 2, 3, 4, 5, 6"
        else:
            try:
                """Check if country is valid"""
                if int(self.country_text_input.text) < 0:
                    self.root.ids.bottomLayout.text = "Country must be >= 0"
                else:
                    self.place_list.add_place(self.city_text_input.text, int(self.country_text_input.text),
                                              self.priority_text_input.text)
                    self.place_list.sort(self.spinner.text)
                    self.clear_text()
                    self.root.ids.rightLayout.clear_widgets()
                    self.build_right_widgets()
            except ValueError:
                self.root.ids.bottomLayout.text = "Please enter a valid number"

    def on_stop(self):
        """Saving places into csv file"""
        self.place_list.save_places()

    pass


if __name__ == '__main__':
    PlacesToVisitApp().run()
