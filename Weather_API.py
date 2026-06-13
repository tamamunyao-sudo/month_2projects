import tkinter as tk
import requests

window = tk.Tk()
window.title("WEATHER API")
window.geometry("1000x500")

city_name = tk.Label(window, text="City Name")
city_name.pack()

entry1 = tk.Entry(window)
entry1.pack()

result = tk.Label(window, text="Result: ")
result.pack()

listbox = tk.Listbox(window)
listbox.pack()

def program():
    city_name = entry1.get()
    city_name = city_name.lower()

    try:
        city_url = "https://geocoding-api.open-meteo.com/v1/search?name="
        city_url = city_url + city_name
        response = requests.get(city_url)
        if response.status_code == 200:
            result.config(text="Results: Success!")
            data = response.json()
            lat = data["results"][0]["latitude"]
            lon = data["results"][0]["longitude"]
            listbox.insert(tk.END, f"Latitude: {lat}")
            listbox.insert(tk.END, f"Longitude: {lon}")

            weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
            response = requests.get(weather_url)
            if response.status_code == 200:
                weather_data = response.json()
                temperature = weather_data["current_weather"]["temperature"]
                windspeed = weather_data["current_weather"]["windspeed"]

                listbox.insert(tk.END, f"Temperature: {temperature}")
                listbox.insert(tk.END, f"Wind Speed: {windspeed}")

                entry1.delete(0, tk.END)
            else:
                result.config(text="Results: City Found but Weather Unavailable!")

        elif response.status_code == 404:
            result.config(text="City Not Found")

        elif response.status_code == 500:
            result.config(text="Server Error")

    except requests.exceptions.RequestException as e:
        print(e)

button = tk.Button(window, text="Search", command=program)
button.pack()

window.mainloop()