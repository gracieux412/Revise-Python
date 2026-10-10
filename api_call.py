import requests


latitude = 48.5
longitude = 2.3

#base url
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m"

response = requests.get(url)
data = response.json()

temp = data['hourly']['temperature_2m']
#print(data)
# print(temp)



def get_weather(latitude, longitude):
    base_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m"
    response = requests.get(base_url)
    data = response.json()
    return data['current']['temperature_2m']

paris_temp = get_weather(48.8566, 2.3522)

print(f"The current temperature in Paris is {paris_temp}°C")




