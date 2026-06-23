import requests
from bs4 import BeautifulSoup
import json
import tkinter as tk

window = tk.Tk()
window.title("BOOK SYSTEM")
window.geometry("1000x500")
book_list = []

for page in range(1, 21):
    url = f"https://books.toscrape.com/catalogue/page-{page}.html"
    response = requests.get(url)

    html1 = response.text
    soup = BeautifulSoup(html1, "html.parser")

    books1 = soup.find_all("article", class_="product_pod")
    for book in books1:
        title = book.find("h3").find("a").text
        price = book.find("p", class_="price_color").text
        price = float(price.replace("Â£", ""))
        if price < 30:
            book_dict = {
                "title": title,
                "price": price,
            }
            book_list.append(book_dict)

with open("books.json", "w") as file:
    json.dump(book_list, file)

with open("books.json", "r") as file:
    book_list = json.load(file)

def display2():
    listbox.delete(0, tk.END)
    for book in book_list:
        title = book["title"]
        price = book["price"]
        if entry1.get() in book["title"]:
            listbox.insert(tk.END, f"{title}: {price}")

book_search = tk.Label(window, text="Enter Book Title")
book_search.pack()

entry1 = tk.Entry(window)
entry1.pack()

search_button = tk.Button(window, text="Search", command=display2)
search_button.pack()

listbox = tk.Listbox(window)
listbox.pack()

def display():
    for book in book_list:
        title = book["title"]
        price = book["price"]
        listbox.insert(tk.END, f"{title}: £{price}")

def cheapest():
    cheapest_title = book_list[0]["title"]
    cheapest_price = book_list[0]["price"]
    for book in book_list:
        title = book["title"]
        price = book["price"]

        if price < cheapest_price:
            cheapest_title = title
            cheapest_price = price

    listbox.insert(tk.END, f"Cheapest Title: {cheapest_title} - £{cheapest_price}")

def most_expensive():
    most_expensive_title = book_list[0]["title"]
    most_expensive_price = book_list[0]["price"]
    for book in book_list:
        title = book["title"]
        price = book["price"]

        if price > most_expensive_price:
            most_expensive_title = title
            most_expensive_price = price

    listbox.insert(tk.END, f"Most Expensive Title: {most_expensive_title} - £{most_expensive_price}")

def average_price():
    total = 0
    for book in book_list:
        total += book["price"]

    average_price = (total / len(book_list))
    listbox.insert(tk.END, f"Average Price: £{average_price}")

def clear():
    listbox.delete(0, tk.END)

def menu():
    Button1 = tk.Button(window, text="View All", command=display)
    Button1.pack()
    Button2 = tk.Button(window, text="Cheapest", command=cheapest)
    Button2.pack()
    Button3 = tk.Button(window, text="Most Expensive", command=most_expensive)
    Button3.pack()
    Button4 = tk.Button(window, text="Average Price", command=average_price)
    Button4.pack()
    Button5 = tk.Button(window, text="Clear", command=clear)
    Button5.pack()

menu()
window.mainloop()

