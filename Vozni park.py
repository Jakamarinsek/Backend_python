class Cars:
    def __init__(self, znamka, model, st_km, leto_ser):
        self.znamka = znamka
        self.model = model
        self.st_km = st_km
        self.leto_ser = leto_ser

    def get_full_list(self):
        return self.znamka + " " + self.model + " " + self.st_km + " " + self.leto_ser

def list_all_cars(cars):
    for index, vehicle in enumerate(cars):
        print "ID: " + str(index)
        print vehicle.get_full_list()

        print ""

def add_new_cars(cars):
    znamka = raw_input("Vnesite znamko avtomobila: ")
    model = raw_input("Vnesite model avtomobila: ")
    st_km = raw_input("Vnesie stanje stevca kilometrov: ")
    leto_ser = raw_input("Vnesite leto zadnjega servisa: ")

    new = Cars(znamka=znamka, model=model, st_km=st_km, leto_ser=leto_ser)
    cars.append(new)

    print ""
    print new.get_full_list() + " was successfully added to your car list."

def edit_cars(cars):
    print "List of the cars available for edit: "

    for index, vehicle in enumerate(cars):
        print str(index) + ") " + vehicle.get_full_list()

    print ""
    selected_id = raw_input("What car would you like to edit? (enter ID number): ")
    selected_car = cars[int(selected_id)]
    print""

    new_km_num = raw_input("Please enter new number of km for %s: " % selected_car.get_full_list())
    selected_car.st_km = new_km_num
    print "Number of km updated."
    print ""

def delete_car(cars):
    print "Select the number of the car you'd like to delete:"

    for index, vehicle in enumerate(cars):
        print str(index) + ") " + vehicle.get_full_list()

    print ""
    selected_id = raw_input("What car would you like to delete? (enter ID number): ")
    selected_car = cars[int(selected_id)]

    cars.remove(selected_car)
    print ""
    print "Car was successfully removed from your contact list."


def main():
    print "Welcome to your Car List"

    vozilo = Cars(znamka="bmw", model="320i", st_km="14000", leto_ser="1979")
    cars = [vozilo]

    while True:
        print ""
        print "Please choose one of these options:"
        print "a) See all your cars"
        print "b) Add a new car"
        print "c) Edit a car"
        print "d) Delete a car"
        print "e) Quit the program."
        print ""

        selection = raw_input("Enter your selection (a, b, c, d or e): ")
        print ""

        if selection.lower() == "a":
            list_all_cars(cars)
        elif selection.lower() == "b":
            add_new_cars(cars)
        elif selection.lower() == "c":
            edit_cars(cars)
        elif selection.lower() == "d":
            delete_car(cars)
        elif selection.lower() == "e":
            print "Thank you for using Car List. Goodbye!"
            break

if __name__ == "__main__":
    main()