from hotel_system import Hotel, Room, Customer


def main():
    my_hotel = Hotel("PrimeHotel")

    # ოთახების დამატება (უკვე სწორი პარამეტრებით)
    my_hotel.add_room_to_hotel(Room(101, "Single", 120.0))
    my_hotel.add_room_to_hotel(Room(102, "Suite", 250.0))
    my_hotel.add_room_to_hotel(Room(103, "Family", 180.0))

    while True:
        print("\n--- სასტუმროს მართვის სისტემა ---")
        print("1. თავისუფალი ოთახების ნახვა")
        print("2. ოთახის დაჯავშნა")
        print("3. ყველა ჯავშნის ნახვა")
        print("4. გამოსვლა")

        choice = input("აირჩიეთ მოქმედება (1-4): ")

        if choice == "1":
            rooms = my_hotel.get_available_rooms()
            if not rooms:
                print("თავისუფალი ოთახები არ არის.")
            for room in rooms:
                print(f"ოთახი {room.room_number} ({room.room_type}) - {room.price}₾")

        elif choice == "2":
            name = input("შეიყვანეთ კლიენტის სახელი: ")
            cust_id = input("შეიყვანეთ კლიენტის ID: ")
            customer = Customer(name, cust_id)

            room_num = int(input("შეიყვანეთ ოთახის ნომერი: "))
            days = int(input("რამდენი ღამით გსურთ დაჯავშნა?: "))

            result = my_hotel.make_reservation(customer, room_num, days)
            print(result)

        elif choice == "3":
            if not my_hotel.reservations:
                print("აქტიური ჯავშნები არ იძებნება.")
            for res in my_hotel.reservations:
                print(
                    f"კლიენტი: {res.customer.name}, ოთახი: {res.room.room_number}, დღეები: {res.days}, სულ: {res.total_cost}₾")

        elif choice == "4":
            print("გმადლობთ, რომ სარგებლობთ ჩვენი სისტემით!")
            break
        else:
            print("არასწორი არჩევანი, სცადეთ თავიდან.")


if __name__ == "__main__":
    main()