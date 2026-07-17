from hotel_system import Hotel, Room, Customer


def main():
    # 1. სასტუმროს და ოთახების შექმნა
    my_hotel = Hotel("პრაიმ სასტუმრო")
    my_hotel.add_room_to_hotel(Room(101, "Single", 50.0, 1))
    my_hotel.add_room_to_hotel(Room(102, "Double", 80.0, 2))
    my_hotel.add_room_to_hotel(Room(201, "Suite", 150.0, 4))
    my_hotel.add_room_to_hotel(Room(202, "Double", 90.0, 2))

    print(f"მოგესალმებით სასტუმროს დაჯავშნის სისტემაში: '{my_hotel.name}'")

    # 2. მომხმარებლის რეგისტრაცია კონსოლში
    name = input("შემოიყვანეთ თქვენი სახელი: ")
    budget = float(input("შემოიყვანეთ თქვენი ბიუჯეტი (ლარი): "))
    customer = Customer(name, budget)

    while True:
        print("\n=== მენიუ ===")
        print("1. თავისუფალი ოთახების ნახვა")
        print("2. ოთახის დაჯავშნა")
        print("3. დაჯავშნის გაუქმება")
        print("4. ჩემი სტატუსის/ბიუჯეტის ნახვა")
        print("5. პროგრამიდან გასვლა")

        choice = input("აირჩიეთ მოქმედება (1-5): ")

        if choice == "1":
            print("\n--- თავისუფალი ოთახები ---")
            r_type = input("მიუთითეთ სასურველი ტიპი (Single/Double/Suite) ან დააჭირეთ Enter-ს ყველასთვის: ")
            search_type = r_type if r_type != "" else None
            available_rooms = my_hotel.show_available_rooms(search_type)

            if not available_rooms:
                print("სამწუხაროდ, თავისუფალი ოთახები არ მოიძებნა.")
            for room in available_rooms:
                print(room)

        elif choice == "2":
            try:
                r_number = int(input("შემოიყვანეთ ოთახის ნომერი: "))
                nights = int(input("რამდენი ღამით გსურთ დაჯავშნა?: "))

                success = my_hotel.book_room_for_customer(customer, r_number, nights)
                if success:
                    print(f"წარმატება! ოთახი N{r_number} წარმატებით დაიჯავშნა.")
            except ValueError:
                print("გთხოვთ შემოიყვანოთ სწორი ციფრები!")

        elif choice == "3":
            try:
                r_number = int(input("შემოიყვანეთ გასაუქმებელი ოთახის ნომერი: "))
                my_hotel.cancel_booking(customer, r_number)
            except ValueError:
                print("გთხოვთ შემოიყვანოთ სწორი ციფრები!")

        elif choice == "4":
            customer.show_booking_summary()

        elif choice == "5":
            print("გმადლობთ, რომ სარგებლობთ ჩვენი სისტემით!")
            break
        else:
            print("არასწორი არჩევანი, სცადეთ თავიდან.")


if __name__ == "__main__":
    main()