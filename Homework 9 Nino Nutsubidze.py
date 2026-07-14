from dataclasses import dataclass

# ==============================================================================
# #1 ამოცანა 1: BankAccount (ინკაფსულაცია და დახურული ატრიბუტები)
# ==============================================================================
print("--- ამოცანა #1: BankAccount ---")

class BankAccount:
    def __init__(self, owner, balance=0):
        self.__owner = owner
        self.__balance = balance  # დახურული ატრიბუტი

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"დაემატა: {amount}. ახალი ბალანსი: {self.__balance}")
        else:
            print("თანხა უნდა იყოს დადებითი!")

    def withdraw(self, amount):
        if amount <= 0:
            print("არასწორი თანხა!")
        elif amount > self.__balance:
            print("არასაკმარისი თანხა! ბალანსი მინუსში ვერ გადავა.")
        else:
            self.__balance -= amount
            print(f"გამოტანილია: {amount}. ნაშთი: {self.__balance}")

    def get_balance(self):
        return self.__balance

# შემოწმება
account = BankAccount("ნუცა", 100)
account.deposit(50)
account.withdraw(30)
account.withdraw(200)  # მინუსში არ გადაუშვებს
print("მიმდინარე ბალანსი (მეთოდით):", account.get_balance())
# print(account.__balance)  # ეს ხაზი ერორს მოგვცემს, რადგან პირდაპირი წვდომა დახურულია


# ==============================================================================
# #2 ამოცანა 2: ShoppingCart (Magic მეთოდები __len__ და __eq__)
# ==============================================================================
print("\n--- ამოცანა #2: ShoppingCart ---")

class ShoppingCart:
    def __init__(self, items_list):
        self.items = items_list  # პროდუქტების სია

    def __len__(self):
        return len(self.items)

    def __eq__(self, other):
        if isinstance(other, ShoppingCart):
            return len(self) == len(other)
        return False

# კალათების შექმნა
cart1 = ShoppingCart(["apple", "banana"])
cart2 = ShoppingCart(["milk", "bread"])
cart3 = ShoppingCart(["water", "juice", "coffee"])
cart4 = ShoppingCart(["cheese", "meat"])

# 2 კალათის შედარება
print(f"კალათა 1 ტოლია კალათა 2-ის? -> {cart1 == cart2}")

# 3 კალათის შედარება
print(f"კალათა 1 ტოლია კალათა 2-ის და კალათა 3-ის? -> {cart1 == cart2 == cart3}")

# 4 კალათის შედარება (1, 2 და 4 ტოლია რაოდენობით, 3 განსხვავებულია)
print(f"კალათა 1, 2 და 4 ტოლია? -> {cart1 == cart2 == cart4}")


# ==============================================================================
# #3 ამოცანა 3: Book (@dataclass მოდული)
# ==============================================================================
print("\n--- ამოცანა #3: Book (@dataclass) ---")

@dataclass
class Book:
    title: str
    author: str
    year: int

    def is_classic(self):
        return self.year < 1970

# წიგნების შექმნა და შემოწმება
book1 = Book("ვეფხისტყაოსანი", "შოთა რუსთაველი", 1200)
book2 = Book("Harry Potter", "J.K. Rowling", 1997)

print(f"არის '{book1.title}' კლასიკა? -> {book1.is_classic()}")
print(f"არის '{book2.title}' კლასიკა? -> {book2.is_classic()}")


# ==============================================================================
# #4 ამოცანა 4: Person (Garbage Collector და __del__)
# ==============================================================================
print("\n--- ამოცანა #4: Person და Garbage Collector ---")

class Person:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print("Person removed")

# ობიექტის შექმნა
p1 = Person("გიორგი")
# წაშლა del-ით მყისიერი რეაგირებისთვის
del p1


# ==============================================================================
# #5 ამოცანა 5: Temperature (Get/Set Properties)
# ==============================================================================
print("\n--- ამოცანა #5: Temperature Properties ---")

class Temperature:
    def __init__(self, celsius=0):
        self.__celsius = celsius

    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, value):
        self.__celsius = value

    @property
    def fahrenheit(self):
        # ცელსიუსის ფარენჰეიტში გადაყვანის ფორმულა: (C * 9/5) + 32
        return (self.__celsius * 9 / 5) + 32

# შემოწმება
t = Temperature(25)
print(f"25°C ფარენჰეიტში არის: {t.fahrenheit}°F")

# ვცვლით ცელსიუსს და ვამოწმებთ, იცვლება თუ არა ფარენჰეიტი ავტომატურად
t.celsius = 0
print(f"ცელსიუსის 0-ზე შეცვლის შემდეგ ფარენჰეიტი არის: {t.fahrenheit}°F")


# ==============================================================================
# #6 ამოცანა 6: CustomList (ინდექსაცია და ციკლი)
# ==============================================================================
print("\n--- ამოცანა #6: CustomList (Iterable) ---")

class CustomList:
    def __init__(self, initial_data=None):
        self.data = initial_data if initial_data is not None else []

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value

    def __iter__(self):
        return iter(self.data)

# შემოწმება
my_list = CustomList([10, 20, 30])
print("ელემენტი მე-1 ინდექსზე:", my_list[1])

my_list[1] = 99  # ვცვლით ელემენტს __setitem__-ით
print("შეცვლის შემდეგ მე-1 ინდექსი:", my_list[1])

print("for ციკლით დაბეჭდვა (__iter__):")
for item in my_list:
    print(item)


# ==============================================================================
# #7 ამოცანა 7: Refrigerator (კუთვნილება და სტრინგად ქცევა)
# ==============================================================================
print("\n--- ამოცანა #7: Refrigerator ---")

class Refrigerator:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def __contains__(self, item):
        return item in self.items

    def __str__(self):
        return f"Fridge with {len(self.items)} items"

    def __del__(self):
        print("Fridge unplugged!")

# შემოწმება
fridge = Refrigerator()
fridge.add_item("milk")
fridge.add_item("cheese")
fridge.add_item("eggs")

print("არის რძე მაცივარში? ->", "milk" in fridge)
print("არის ვაშლი მაცივარში? ->", "apple" in fridge)
print(fridge)  # ბეჭდავს __str__-ს

del fridge  # შლის მაცივარს და ბეჭდავს "Fridge unplugged!"


# ==============================================================================
# #8 ამოცანა 8: FunnyCalculator (ოპერატორების გადატვირთვა)
# ==============================================================================
print("\n--- ამოცანა #8: FunnyCalculator ---")

class FunnyCalculator:
    def __add__(self, other):
        return "Why are you adding numbers? Just buy a calculator"

    def __mul__(self, other):
        return "Multiplication is too mainstream..."

    def __truediv__(self, other):
        # ყურადღება: როცა ვწერთ 10 / calc, გამოიძახება __rtruediv__,
        # ხოლო თუ calc / 0 წერია — მაშინ გამოიძახება __truediv__.
        # ორივე შემთხვევისთვის რომ კარგად იმუშაოს, ასე ავაწყოთ:
        if other == 0:
            return "ZeroDivisionError? Nah, let’s just say infinity"
        return "Division is boring..."

    def __rtruediv__(self, other):
        # ეს მეთოდია საჭირო, როცა რიცხვი იყოფა კალკულატორზე (10 / calc)
        return "ZeroDivisionError? Nah, let’s just say infinity"

    def __str__(self):
        return "I’m the funniest calculator in Python!"

# შემოწმება
calc = FunnyCalculator()
print(calc)
print("calc + 5 ->", calc + 5)
print("calc * 2 ->", calc * 2)
print("10 / calc ->", 10 / calc)