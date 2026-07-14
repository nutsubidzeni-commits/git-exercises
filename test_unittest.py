import unittest

# =====================================================================
# #1 unittest1: Calculator კლასი და მისი ტესტები
# =====================================================================
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("ნულზე გაყოფა შეუძლებელია!")
        return a / b

class TestCalculator(unittest.TestCase):
    def setUp(self):
        # setUp მეთოდი ყოველი ტესტის წინ ქმნის კალკულატორის ახალ ობიექტს
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(5, 3), 8)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)
        self.assertEqual(self.calc.subtract(0, 5), -5)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-2, 3), -6)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        # 0-ზე გაყოფის შემოწმება შეცდომის (ValueError) მოლოდინით
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)


# =====================================================================
# #2 unittest2: BankAccount კლასი და მისი ტესტები
# =====================================================================
class BankAccount:
    def __init__(self, balance=0.0):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("შესატანი თანხა უნდა იყოს დადებითი!")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("ბალანსზე მეტი თანხის გამოტანა შეუძლებელია!")
        if amount <= 0:
            raise ValueError("გამოსატანი თანხა უნდა იყოს დადებითი!")
        self.balance -= amount

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount(100.0) # საწყისი ბალანსი 100.0

    def test_initial_and_correct_balance(self):
        self.assertEqual(self.account.balance, 100.0)
        self.account.deposit(50.0)
        self.assertEqual(self.account.balance, 150.0)
        self.account.withdraw(30.0)
        self.assertEqual(self.account.balance, 120.0)

    def test_negative_deposit_error(self):
        # უარყოფითი თანხის შეტანისას შეცდომის შემოწმება
        with self.assertRaises(ValueError):
            self.account.deposit(-20)

    def test_withdraw_more_than_balance_error(self):
        # ბალანსზე მეტი თანხის გამოტანისას შეცდომის შემოწმება
        with self.assertRaises(ValueError):
            self.account.withdraw(150.0)


# =====================================================================
# #3 unittest3: JSON Status ფუნქცია და მისი ტესტები
# =====================================================================
def get_status_from_response(response: dict):
    if "status" not in response:
        raise KeyError("სტატუსის ველი არ არსებობს JSON response-ში!")
    return response["status"]

class TestJSONResponse(unittest.TestCase):
    def test_status_exists(self):
        mock_response = {"status": "success", "code": 200, "data": []}
        self.assertEqual(get_status_from_response(mock_response), "success")

    def test_status_missing_error(self):
        mock_bad_response = {"error_msg": "Not Found", "code": 404}
        # თუ სტატუსი არ არსებობს, უნდა ვისროლოთ KeyError
        with self.assertRaises(KeyError):
            get_status_from_response(mock_bad_response)

if __name__ == '__main__':
    unittest.main()

    