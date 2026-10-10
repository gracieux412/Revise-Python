#when print is used in the function you just call the function
def greet():
    print("Hello world")

greet()
# when return is used, you print
def greet2():
    return "Hello world"

print(greet2())

# ------------------------------------------------


def calculate_price():
    price = 100 #local variables
    tax = price * 0.1 #local variables
    print(f"Total: {price + tax}")

calculate_price()  # Total: 110

# This fails - price doesn't exist outside the function
#print(price)  # NameError: name 'price' is not defined

#global variable example.

discount_rate = 0.15

def apply_discount(price):
    discount = price * discount_rate
    return price - discount

result = apply_discount(100)
print(result)

# ---------- to modify global variables with global key word ---------------------

counter = 0  # Global variable

def increment():
    global counter  # Declare we want to modify the global variable
    counter += 1

increment()
increment()
print(counter)  # 2

# --------------------- Good - using parameters and return

def add_amounts(current_total, amount):
    return current_total + amount

total = 0
total = add_amounts(total, 10)
total = add_amounts(total, 20)
print(total)  # 30

# ---------------------calc price

def calculate_price(price, tax_rate, discount):
    tax = price * tax_rate
    final_price = price + tax - discount
    return final_price

price = calculate_price(100, 0.011, 10)
print(f"the final price is Ugx {price}")

# - ------------ parameters with default values

def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

# Use default
greet("Alice")           # Hello, Alice!

# Override default
greet("Bob", "Hi")       # Hi, Bob!
greet("Charlie", "Hey")  # Hey, Charlie!


#-------------------------------------------------------

def double(number):
    return number * 2

# Store in variable
result = double(5)

# Use in expressions
total = double(5) + double(3)  # 10 + 6 = 16

# Pass to other functions
print(double(10))  # 20

# Use in conditions
if double(7) > 10:
    print("Big number!")


# function that return an tuple with min and max value in a list

def get_min_max(numbers):
    return min(numbers), max(numbers)

result = get_min_max([5, 3,10,5,20])
print(result)

min, max = get_min_max([5, 3,10,5,20])
print(f"Min: {min}, Max: {max}")