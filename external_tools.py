import math
from math import sqrt, pi
import random
import datetime
import os
import json
import pandas as pd

#use pandas
data = [{"name":"kitsa"}]
df = pd.DataFrame(data)
print(df)

data = {"name": "Alice", "age": 30}
json_string = json.dumps(data)
print(json_string)


current_dir = os.getcwd()
print(current_dir)

today = datetime.date.today()
print(today)

number = random.randint(1, 10)
print(number)
radius = 5
circle_area = pi * radius ** 2
print(circle_area)

print(sqrt(16))  # 4.0
print(pi)        # 3.141592653589793

#------------- Using external packages ------------------------

import requests

try:
    response = requests.get("https://api.example.com/data")
    requests.status_codes(200)
    data = response.json()
    print(data)
except requests.exceptions.RequestException as error:
    print(error)

# ------------------------------------------------------------

data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['NYC', 'LA', 'Chicago']
}
df = pd.DataFrame(data)
print(df)


