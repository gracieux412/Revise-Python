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