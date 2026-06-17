import itertools
import calendar
from datetime import datetime, timedelta

print("--- სავარჯიშო #1 ---")
word = "ABCD"
permutations = list(itertools.permutations(word))
for p in permutations:
    print("".join(p))
print(f"სულ რაოდენობა: {len(permutations)}")

print("\n--- სავარჯიშო #2 ---")
today = datetime.now()
days_until_next_monday = (7 - today.weekday()) % 7
if days_until_next_monday == 0:
    days_until_next_monday = 7
next_monday = today + timedelta(days=days_until_next_monday)
next_tuesday = next_monday + timedelta(days=1)
print(f"მომდევნო კვირის პირველი სამშაბათი: {next_tuesday.strftime('%Y-%m-%d')}")

print("\n--- სავარჯიშო #3 ---")
myinput = int(input("შეიყვანეთ წელი (მაგ. 2026): "))
if calendar.isleap(myinput):
    print(f"{myinput} არის ნაკიანი წელი.")
else:
    print(f"{myinput} არ არის ნაკიანი წელი.")

print("\n--- სავარჯიშო #4 ---")
next_new_year = datetime(today.year + 1, 1, 1)
days_left = (next_new_year - today).days
weeks_left = days_left / 7
print(f"ახალ წლამდე დარჩენილია: {weeks_left:.1f} კვირა")

print("\n--- სავარჯიშო #5 ---")
numbers = [1, 2, 3, 4, 5]
combinations = list(itertools.combinations(numbers, 3))
for combo in combinations:
    print(combo)

print("\n--- სავარჯიშო #6 ---")
word_xyz = "XYZ"
for length in range(1, 4):
    for combo in itertools.combinations(word_xyz, length):
        print("".join(combo))

print("\n" + "=" * 20 + "\n")


import random
import time
import itertools
from datetime import datetime, timedelta, date

print("--- სავარჯიშო #7 ---")
secret_number = random.randint(1, 20)
print("კომპიუტერმა ჩაიფიქრა რიცხვი 1-20 მდე. გაქვს 5 წამი გამოსაცნობად!")
start_time = time.time()
user_guess = input("შეიყვანე რიცხვი: ")
end_time = time.time()

if end_time - start_time > 5:
    print("დრო ამოიწურა, თქვენ დამარცხდით.")
else:
    if int(user_guess) == secret_number:
        print("სწორია! გაიმარჯვეთ!")
    else:
        print(f"ვერ გამოიცანით. სწორი პასუხი იყო: {secret_number}")


print("\n--- სავარჯიშო #8 ---")
start = datetime.now()
player1 = start + timedelta(seconds=random.randint(5, 20))
player2 = start + timedelta(seconds=random.randint(5, 20))
print(f"მოთამაშე 1 ფინიში: {player1.strftime('%H:%M:%S')}")
print(f"მოთამაშე 2 ფინიში: {player2.strftime('%H:%M:%S')}")
if player1 < player2:
    print("პირველმა მოთამაშემ ნაკლებ დროში დაასრულა!")
elif player2 < player1:
    print("მეორე მოთამაშემ ნაკლებ დროში დაასრულა!")
else:
    print("ფრეა!")


print("\n--- სავარჯიშო #9 ---")
print("შეიყვანეთ დაბადების თარიღი:")
b_year = int(input("წელი: "))
b_month = int(input("თვე: "))
b_day = int(input("დღე: "))
today_date = date.today()
next_birthday = date(today_date.year, b_month, b_day)
if next_birthday < today_date:
    next_birthday = date(today_date.year + 1, b_month, b_day)
days_to_birthday = (next_birthday - today_date).days
print(f"შემდეგ დაბადების დღემდე დარჩენილია: {days_to_birthday} დღე")


print("\n--- სავარჯიშო #10 ---")
digits = "123456"
correct_password = "".join(random.choices(digits, k=4))
print(f"(სისტემური მინიშნება, რეალური პაროლია: {correct_password})")

all_combos = itertools.product(digits, repeat=4)
for combo in all_combos:
    current_try = "".join(combo)
    print(f"ვცდით პაროლს: {current_try}")
    if current_try == correct_password:
        print("პაროლი სწორია, საცავი გახსნილია!")
        break