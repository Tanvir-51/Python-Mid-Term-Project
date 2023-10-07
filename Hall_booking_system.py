from datetime import datetime

class Star_Cinema:
    _hall_list = []

    @classmethod
    def entry_hall(cls, hall):
        cls._hall_list.append(hall)

    @classmethod
    def get_hall_list(cls):
        return cls._hall_list


class Hall:
    def __init__(self, rows, cols, hall_no):
        self._seats = {}
        self._show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        self.entry_hall()

    def entry_hall(self):
        Star_Cinema.entry_hall(self)

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self._show_list.append(show_info)
        self._seats[id] = [['0' for _ in range(self._cols)] for _ in range(self._rows)]

    def book_seats(self, id, seat_list):
        if id not in self._seats:
            raise ValueError("Invalid show ID")

        for row, col in seat_list:
            if row < 1 or row > self._rows or col < 1 or col > self._cols:
                raise ValueError("Invalid seat")

            if self._seats[id][row - 1][col - 1] == '1':
                raise ValueError("Seat already booked")

            self._seats[id][row - 1][col - 1] = '1'

    def view_show_list(self):
        return self._show_list

    def view_available_seats(self, id):
        if id not in self._seats:
            raise ValueError("Invalid show ID")

        return self._seats[id]

    def select_seats(self, id):
        if id not in self._seats:
            raise ValueError("Invalid show ID")

        available_seats = []
        for row in range(1, self._rows + 1):
            for col in range(1, self._cols + 1):
                if self._seats[id][row - 1][col - 1] == '0':
                    available_seats.append((row, col))

        return available_seats

def display_menu():
    print("1. VIEW ALL SHOW TODAY")
    print("2. VIEW AVAILABLE SEATS")
    print("3. BOOK TICKET")
    print("4. EXIT")

current_date = datetime.now().strftime("%Y-%m-%d")

hall1 = Hall(rows=5, cols=5, hall_no=1)

hall1.entry_show(id="111", movie_name="Movie1", time="11:00 AM")
hall1.entry_show(id="222", movie_name="Movie2", time="2:00 PM")

while True:
    display_menu()
    option = input("ENTER OPTION: ")

    if option == '1':
        show_list = hall1.view_show_list()
        print("-" * 85)
        for show in show_list:
            show_id, movie_name, show_time = show
            print(f"MOVIE NAME: {movie_name}({show_id}) SHOW ID: {show_id} DATE: {current_date} TIME: {show_time}")
        print("-" * 85)
    
    elif option == '2':
        show_id = input("Enter the show ID: ")
        available_seats = hall1.view_available_seats(show_id)
        print(f"Available Seats for {show_id}:")
        for row in available_seats:
            print(" ".join(row))

    elif option == '3':
        show_id = input("Enter the show ID: ")
        num_tickets = int(input("Number of Tickets: "))
        selected_seats = []
        for _ in range(num_tickets):
            while True:
                try:
                    row = int(input("Enter Seat Row: "))
                    col = int(input("Enter Seat Col: "))
                    if (row, col) in selected_seats:
                        print("Seat already selected. Please choose another seat.")
                    else:
                        selected_seats.append((row, col))
                        break
                except ValueError:
                    print("Invalid input. Please enter valid row and seat numbers.")

        try:
            hall1.book_seats(show_id, selected_seats)
            for seat in selected_seats:
                print(f"Seat {seat} booked for show {show_id}")
        except ValueError as e:
            print(f"Error: {e}")

    elif option == '4':
        print("Exiting the program.")
        break

    else:
        print("Invalid option. Please select a valid option.")
