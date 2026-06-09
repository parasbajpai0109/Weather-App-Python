import requests
while True:
    print("       Welcome to Weather-App")
    city = input("Enter City Name (eg: Delhi, India) ('q' for Exit): ")

    if city.lower() == 'q':
        print("Thanks for using Weather-app")
        break

    api_key = "YOUR API KEY"
    url =f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

    response = requests.get(url)
    data = response.json()

    if "error" in data:
        print("City Not Found")

    else:
        print(f"       Weather report of {city}")
        city_name = data['location']['name']
        print(f"City Name: {city_name}")

        region_name = data['location']['region']
        print(f"Region Name: {region_name}")

        country_name = data['location']['country']
        print(f"Country Name: {country_name}")

        local_time = data['location']['localtime']
        print(f"Local Time {local_time}")

        temp = data['current']['temp_c']
        print(f"Temperature: {temp}°C")

        feels_like = data['current']['feelslike_c']
        print(f"Feels Like: {feels_like}°C")

        humidity = data['current']['humidity']
        print(f"Humidity: {humidity}%")

        wind_speed = data['current']['wind_kph']
        print(f"Wind Speed: {wind_speed} km/h")

        condition = data['current']['condition']['text']
        print(f"Condition: {condition}")

