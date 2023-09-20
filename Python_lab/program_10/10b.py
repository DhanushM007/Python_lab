import json

with open("C:\\Users\\jaswa\\Desktop\\weather.json.txt") as f:
    data=json.load(f)
    
current_temp=data["main"]["temp"]
humidity=data["main"]["humidity"]
weather_desc=data["weather"][0]["description"]

print(f'current temperature:{current_temp}°C')
print(f'Humidity:{humidity}%')
print(f'weather decription:{weather_desc}')