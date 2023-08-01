import requests

API_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

def get_weather_data():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()["list"]
    else:
        print("Failed to fetch weather data. Please try again later.")
        return None

def get_temperature(date):
    weather_data = get_weather_data()
    if weather_data:
        for item in weather_data:
            if date in item["dt_txt"]:
                return item["main"]["temp"]
        print("No data found for given date.")
    return None

def get_wind_speed(date):
    weather_data = get_weather_data()
    if weather_data:
        for item in weather_data:
            if date in item["dt_txt"]:
                return item["wind"]["speed"]
        print("No data found for given date.")
    return None

def get_pressure(date):
    weather_data = get_weather_data()
    if weather_data:
        for item in weather_data:
            if date in item["dt_txt"]:
                return item["main"]["pressure"]
        print("No data found for given date.")
    return None

def main():
    while True:
        print("\nWeather API\nOptions:")
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = input("Enter your choice (0-3): ")

        if choice == "1":
            date = input("Enter the date (yyyy-mm-dd HH:MM:SS format): ")
            temperature = get_temperature(date)
            if temperature:
                print(f"The temperature on {date} is {temperature} K.")

        elif choice == "2":
            date = input("Enter the date (yyyy-mm-dd HH:MM:SS format): ")
            wind_speed = get_wind_speed(date)
            if wind_speed:
                print(f"The wind speed on {date} is {wind_speed} m/s.")

        elif choice == "3":
            date = input("Enter the date (yyyy-mm-dd HH:MM:SS format): ")
            pressure = get_pressure(date)
            if pressure:
                print(f"The pressure on {date} is {pressure} hPa.")

        elif choice == "0":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
