import logging

# ლოგირების გამართვა: ინახავს დაჯავშნებს "hotel_bookings.log" ფაილში
logging.basicConfig(
    filename="hotel_bookings.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

class Room:
    def __init__(self, room_number: int, room_type: str, price_per_night: float, max_guests: int):
        self.room_number = room_number
        self.room_type = room_type
        self.price_per_night = price_per_night
        self.is_available = True
        self.max_guests = max_guests

    def book_room(self):
        self.is_available = False

    def release_room(self):
        self.is_available = True

    def calculate_price(self, nights: int) -> float:
        return self.price_per_night * nights

    def __str__(self):
        status = "თავისუფალი" if self.is_available else "დაკავებული"
        return f"ოთახი N{self.room_number} ({self.room_type}) - {self.price_per_night} ლარი/ღამე | სტატუსი: {status}"


class Customer:
    def __init__(self, name: str, budget: float):
        self.name = name
        self.budget = budget
        self.booked_rooms = []
        self.reward_points = 0

    def add_room(self, room: Room):
        self.booked_rooms.append(room)

    def remove_room(self, room: Room):
        if room in self.booked_rooms:
            self.booked_rooms.remove(room)

    def pay_for_booking(self, total_price: float) -> bool:
        if self.budget >= total_price:
            self.budget -= total_price
            # ბონუს ქულების დაგროვება (მაგალითად, გადახდილი თანხის 10%)
            self.reward_points += int(total_price * 0.1)
            return True
        return False

    def show_booking_summary(self):
        print(f"\n--- დაჯავშნის რეზიუმე: {self.name} ---")
        print(f"მიმდინარე ბიუჯეტი: {self.budget} ლარი")
        print(f"დაგროვილი ქულები: {self.reward_points}")
        print("დაჯავშნილი ოთახები:")
        if not self.booked_rooms:
            print(" - არცერთი ოთახი არ არის დაჯავშნილი.")
        for room in self.booked_rooms:
            print(f" - ოთახი N{room.room_number} ({room.room_type})")


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.bookings_log = []

    def add_room_to_hotel(self, room: Room):
        self.rooms.append(room)

    def show_available_rooms(self, room_type: str = None) -> list:
        available = []
        for room in self.rooms:
            if room.is_available:
                if room_type is None or room.room_type.lower() == room_type.lower():
                    available.append(room)
        return available

    def calculate_total_booking(self, room_number: int, nights: int) -> float:
        for room in self.rooms:
            if room.room_number == room_number:
                return room.calculate_price(nights)
        return 0.0

    def log_booking(self, customer: Customer, room: Room, total_price: float):
        log_message = f"მომხმარებელი: {customer.name}, დაჯავშნა ოთახი N{room.room_number}, ჯამური ფასი: {total_price} ლარი"
        self.bookings_log.append(log_message)
        logging.info(log_message)

    def book_room_for_customer(self, customer: Customer, room_number: int, nights: int) -> bool:
        for room in self.rooms:
            if room.room_number == room_number:
                if room.is_available:
                    total_price = room.calculate_price(nights)
                    if customer.pay_for_booking(total_price):
                        room.book_room()
                        customer.add_room(room)
                        self.log_booking(customer, room, total_price)
                        return True
                    else:
                        print("შეცდომა: არასაკმარისი ბიუჯეტი!")
                        return False
                else:
                    print("შეცდომა: ოთახი უკვე დაკავებულია!")
                    return False
        print("შეცდომა: ოთახი ვერ მოიძებნა!")
        return False

    def cancel_booking(self, customer: Customer, room_number: int):
        for room in customer.booked_rooms:
            if room.room_number == room_number:
                room.release_room()
                customer.remove_room(room)
                log_message = f"დაჯავშნა გაუქმდა - მომხმარებელი: {customer.name}, ოთახი N{room_number}"
                self.bookings_log.append(log_message)
                logging.info(log_message)
                print(f"წარმატება: ოთახი N{room_number} გათავისუფლდა!")
                return
        print("შეცდომა: ეს ოთახი არ არის ამ მომხმარებლის მიერ დაჯავშნილი!")
