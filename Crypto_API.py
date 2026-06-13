import tkinter as tk
import requests

window = tk.Tk()
window.title("Crypto API")
window.geometry("1000x500")

crypto_type = tk.Label(window, text="Enter the Crypto Type: ", font = ("Arial", 30, "bold"))
crypto_type.pack()

entry1 = tk.Entry(window, width=50, font = ("Arial", 20))
entry1.pack()

listbox = tk.Listbox(window, font = ("Arial", 15))
listbox.pack()

result = tk.Label(window, text="Result: ", font = ("Arial", 15, "bold"))
result.pack()
result.pack()

def program():
    listbox.delete(0, tk.END)

    crypto_type = entry1.get()
    crypto_type = crypto_type.lower()

    try:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_type}&vs_currencies=usd"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            result.config(text="Result: Success!")
            usd_price = data[crypto_type]["usd"]
            listbox.insert(tk.END, f"Crypto: {crypto_type}")
            listbox.insert(tk.END, f"Price: {usd_price}")
            listbox.insert(tk.END, "Currency: USD")

            entry1.delete(0, tk.END)
        elif response.status_code == 404:
            result.config(text="Result: Not Found")
        elif response.status_code == 500:
            result.config(text="Result: Server Error")

    except requests.exceptions.RequestException as e:
        print(e)

button = tk.Button(window, text="Display Price: ", command=program, background="hot pink")
button.pack()

window.mainloop()