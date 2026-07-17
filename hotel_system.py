class Room:
    def __init__(self, room_number, room_type, price):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.is_occupied = False

    def book_room(self):
        if not self.is_occupied:
            self.is_occupied = True
            return True
        return False

    def free_room(self):
        self.is_occupied = False


class Customer:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id


class Reservation:
    def __init__(self, customer, room, days):
        self.customer = customer
        self.room = room
        self.days = days
        self.total_cost = room.price * days


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = {}
        self.reservations = []

    def add_room_to_hotel(self, room):
        self.rooms[room.room_number] = room

    def get_available_rooms(self):
        return [room for room in self.rooms.values() if not room.is_occupied]

    def make_reservation(self, customer, room_number, days):
        if room_number in self.rooms:
            room = self.rooms[room_number]
            if room.book_room():
                res = Reservation(customer, room, days)
                self.reservations.append(res)
                return f"წარმატებული ჯავშანი: {customer.name}-სთვის, ოთახი {room_number}."
        return "სამწუხაროდ, ოთახი დაკავებულია ან არ არსებობს."