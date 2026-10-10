# learning python basically for ai applications.

#usage of packages forexample
import requests


response = requests.get("https://ryanteq.com")
print(f"The status code is {response.status_code}")


#  VARIABLES

name = "Kitsa"
age = 29

print(f"Hello, my name is {name} and I am {age} years old")
print(type(age))

#make a simple decision

if age >= 18:
    print("I can vote")
else:
    print("I'm too young to vote")


#some sample data to work with

numbers = [1, 3, 5, 3, 4]
print(f"then numbers are {numbers}")

#calculate something
total = sum(numbers)
print(f"the total of the numbers is {total}")
# some bit of string concatenation

product = "Maize"
print("The product is "+ product)


user_name = "Gracieux"
user_age = 26
is_student = False
is_logged_in = True

#Realize the value of user age has changed
user_age = 30

#changes it again
user_age = user_age + 5
print(user_age)


# comments in python

def calculate_tip(bill):
    """
    Calculate 20% tip for a restaurant bill.
    Take the bill amount and return the tip.
    """
    return bill * 0.20

calculate_tip(300)

# good comments states why not the obvious

#Discussion on datatypes and type conversion
sum = 10 + 5 + 4
name = "Gracieux" + " Kitsa"

value = "5"
final_sum = int(value) + sum

print(f"The total sum is {final_sum}")

#handling numbers
#power numbers 

squared = 5 ** 2
cubed = 2 ** 3
print(f"squared is {squared} and cubed is {cubed}")

# Divisions use / or // for rounding up

result = 10/3
result2 = 10 // 3
print(f"result 1 is {result} and result 2 is {result2}")

# Dealing with strings.
#use single, double or triple 

paragraph = """ This is
a multi line string
"""

#--------------------------------------------
stars = "*" * 5
print(stars)

# String methods and returns the length of the string.
message = "hello there"
print(len(message))

#Logical operators 

age = 25
has_license = True

# AND - both must be true
can_drive = age >= 16 and has_license
print(can_drive)  # True

# OR - at least one must be true
day = "Saturday"
is_weekend = day == "Saturday" or day == "Sunday"
print(is_weekend)  # True

# NOT - reverses the value
is_adult = age >= 18
is_child = not is_adult
print(is_child)  # False

# AND: Both must be True
print(True and True)    # True
print(True and False)   # False
print(False and False)  # False

# OR: At least one must be True  
print(True or False)    # True
print(False or False)   # False

# NOT: Flips the value
print(not True)         # False
print(not False)        # True


# Interesting part, String manipulation ----------------------

first_name = "Jane"
last_name = "Doe"

# Using +
full_name = first_name + " " + last_name  # "Jane Doe"

# Using f-strings (modern Python way!)
greeting = f"Hello, {first_name}!"  # "Hello, Jane!"

# Multiple variables
age = 25
intro = f"I'm {first_name} and I'm {age} years old"

#string methods changind the cases and cleaning the strings
text = "Python Programming"

print(text.lower())
print(text.upper())
print(text.title())

messy = " hello there "
print(messy.strip())

price ="$19.99"
print(price.strip("$"))

# finding and replacing

message = "I love Python programming with python"

#check if something exists
print("Python" in message)
print(message.startswith("I"))
print(message.endswith("python"))

#finding the string position
print(message.find("Python"))
print(message.count("Python"))

new_message = message.replace("python", "Python")
print(new_message)



#-------------------------------control flow ---------------------
temperature = 25

if temperature > 30:
    print("It's hot!")
else:
    print("Nice weather!")

#if else if

score = 85

if score >= 90:
    print("A - Excellent!")
elif score >= 80:
    print("B - Good job!")
elif score >= 70:
    print("C - Keep it up!")
else:
    print("F - Need improvement")





age = 25
has_license = True
weekend = "Saturday"
is_raining = True
is_weekend = False
is_holiday=True

# Both must be True
if age >= 18 and has_license:
    print("You can drive!")

# At least one must be True
if weekend or is_holiday:
    print("No work today!")

# Reverse the condition
if not is_raining:
    print("Let's go outside!")   


has_ticket = False
age = 19

if has_ticket:
    if age >= 18:
        print("Enjoy the movie!")
    else:
        print("Need Adult supervision")
else:
    print("Buy a ticket first")


#----------------------- Loops ------------------------

for i in range(5):
    print("Hello! Kg")

for i in range(10):
    print(i)

# Count from 1 to 5
for i in range(1, 6):
    print(i)
# Output: 1, 2, 3, 4, 5

# Count by 2s
for i in range(0, 10, 2):
    print(i)
# Output: 0, 2, 4, 6, 8

name = "Ryan"
for letter in name:
    print(letter)


# Loop through a list(preview)
colors = ["red", "blue", "green"]
for color in colors:
    print(color)

#Using while loops 
count = 0 
while count < 5:
    print(f"Count is {count}")
    count += 1  # Increment count by 1


#Data structure and Algorithm 
# Lists are ordered collections and is a versatile data structure.

my_list = []

fruits = ["apple", "banana", "orange"]
numbers = [1, 3, 5, 2, 4]
numbers.sort()
print(numbers)
mixed =["hello", 42, True, 2.32]
students_list= [
    {
        "name": "kitsa",
        "age": 22
    },
    {
        "name": "Ryan",
        "age": 2
    }
]

print(numbers[2:4])
fruits[0]="mango"

for i in numbers:
    print(i)


for student in students_list:
    print(student['name'])

for person in students_list:
    for keys, value in person.items():
        print(f"{keys} : {value}")
        print(person.keys())

# Accessing a single value from a dictionary inside a list

print(students_list[0]["name"])

shopping_list = []

shopping_list.append("Milk")
shopping_list.append("Salt")

shopping_list.extend(["Sugar", "Onions", "Tomatos"])

print(shopping_list)

shopping_list.pop()

print(shopping_list)

# Simple project to capitalize then first letter of those names.

names = ["gracieux kitsa", "ryan john", "alice brown"]

formatted_names = [name.title() for name in names]

formatted_names.sort()

print(formatted_names)


# more list examples


items = ["cooking oil", "spahgetti", "sausage", "pork"]
shopping_list =[]

shopping_list.extend(items)
print(shopping_list)

shopping_list.insert(0, "Maize")
print(shopping_list)



# More on data structure, dictionaries
# This stores data in key-value pairs

#creating a dictionary

# Empty dictionary
my_dict = {}

# Dictionary with data
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Different ways to create
scores = dict(math=95, english=87, science=92, geography="Fail")

print(scores)

person = {"name": "Alice", "age": 30, "city": "New York"}

# Get values by key
print(person["name"])       # "Alice"
print(person["age"])        # 30

# Safer with get()
print(person.get("job"))    # None (no error)
print(person.get("job", "Unknown"))  # "Unknown" (default)

for key, value in person.items():
    print(key, value)

# -------------------------------------------------------

#changing dictionaries

person = {"name":"Alice", "age":30}

person["email"] = "alice@example.com"
person["age"]=31

print(person)

print(person["email"])
del person["email"]
print(person)

person.clear() # remove all
print(person) # empty dictionary


person = {"name": "Alice", "age": 30, "city": "New York"}

# Get all keys, values, or items
print(person.keys())    # dict_keys(['name', 'age', 'city'])
print(person.values())  # dict_values(['Alice', 30, 'New York'])
print(person.items())   # dict_items([('name', 'Alice'), ...])

# Check if key exists
if "name" in person:
    print("Name found!")

# Update multiple values
person.update({"age": 31, "job": "Engineer"})


# Dictionary of dictionaries
students = {
    "alice": {"age": 20, "grade": "A"},
    "bob": {"age": 21, "grade": "B"},
    "charlie": {"age": 19, "grade": "A"}
}

# Access nested data
print(students["alice"]["grade"])  # "A"


# TUPLES 
# Work with immutable sequences.
#they are like lists, but they can't be changed once created.

#eg: coordinates, RGB colors, database records.

empty = ()

#tuple with items
point = (3, 5)
colors = ("red", "green", "blue")

#single items in a tuple is with a comma
single = (42,)
print(type(single))

coordinates = 10, 20
print(type(coordinates))

point = (3, 5)
colors = ("red", "green", "blue")

# Get items
print(point[0])      # 3
print(colors[-1])    # "blue"

# Slicing works too
print(colors[0:2])   # ("red", "green")

######################## Tuple unpacking #####################
 
point = (3, 5)
x, y = point 

print(f"point x is {x}, and point y is {y}")

#multiple assignment
a, b, c = 1, 2, 3

#swap variables 
x, y = y , x
print(x)

#---------------------------
#converting the tuple to a list, manupulate the list and then convert back to a tuple
point = (4,)

temp = list(point)
temp[0]=3

point = tuple(temp)

print(point)
print(type(point))

unique_id = 223, 455, 656, 869

for i in unique_id:
    print(i)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# SETS
#--------------------------------------------------------

empty_set = set()

scores = [20, 30, 55, 20]
unique_scores = set(scores)
print(unique_scores)

colors = {"red", "blue"}

# Add items
colors.add("green")
print(colors)  # {'red', 'blue', 'green'}

# Remove items
colors.remove("blue")    # Error if not found
colors.discard("yellow") # No error if not found

# Check membership
if "red" in colors:
    print("Red is available")


