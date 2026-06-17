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