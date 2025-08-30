class Adder:
    def __init__(self, num1, num2):
        self.number1 = num1
        self.number2 = num2

    def add_numbers(self):
        return self.number1 + self.number2

my_adder = Adder(10, 5)

sum_result = my_adder.add_numbers()

print(f"The sum is: {sum_result}")

