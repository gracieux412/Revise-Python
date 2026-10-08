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