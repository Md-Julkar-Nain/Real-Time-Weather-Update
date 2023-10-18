import requests

city_name = input('Enter Your City: ')

api_key = '1a299c2eba100d6ac4c4a0572317231e'

url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'


"""
Minimum temperature of {city_name} is {} and Maximum is {} and it feels like {}
"""

response = requests.get(url)
data = response.json()

main = data.get('main')

temp_min = main.get('temp_min')
temp_max = main.get('temp_max')
feels_like = main.get('feels_like')
temp = main.get('temp')


print(f'Today\'s Temperature of {city_name} is {temp}. \n'
      f'Minimum Temperature is {temp_min} and Maximum Temperature is {temp_max}. \n'
      f'It Feels Like {feels_like}. '
      f'Thnks for Staying with Us.')