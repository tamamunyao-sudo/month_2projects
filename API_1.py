import requests
import tkinter as tk

window = tk.Tk()
window.title("Country API")
window.geometry("1000x500")

country_name = tk.Label(window, text = "Enter Country Name: ")
country_name.pack()

entry1 = tk.Entry(window)
entry1.pack()

result = tk.Label(window, text = " ")
result.pack()

listbox = tk.Listbox(window, width = 50, height = 10)
listbox.pack()

def program():
    listbox.delete(0, tk.END)

    country_name2 = entry1.get()
    country_name2 = country_name2.lower()

    try:
        country_url = "https://restcountries.com/"
        country_url = country_url + "v3.1/name/" + country_name2
        response = requests.get(country_url)
        if response.status_code == 200:
            country_data = response.json()
            result.config(text = "Success!")
            listbox.insert(tk.END, country_data[0]["capital"])
            listbox.insert(tk.END, country_data[0]["population"])
            listbox.insert(tk.END, country_data[0]["region"])
        elif response.status_code == 404:
            result.config(text = "Not found")
        elif response.status_code == 500:
            result.config(text = "Server Error")
    except requests.exceptions.RequestException as e:
        result.config(text = f"{e}")

    entry1.delete(0, tk.END)

button = tk.Button(window, text = "Press to Display Country Info", command = program)
button.pack()

window.mainloop()
