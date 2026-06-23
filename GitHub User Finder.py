import tkinter as tk
import json
import requests

window = tk.Tk()
window.title("GitHub User Finder")
window.geometry("1000x500")

user_list = []

github_username = tk.Label(window, text="Enter GitHub Username:")
github_username.pack()

entry1 = tk.Entry(window)
entry1.pack()

results = tk.Label(window, text="Result: ")
results.pack()

listbox = tk.Listbox(window, width=30)
listbox.pack()

def program():
    listbox.delete(0, tk.END)
    username = entry1.get()
    url = (f"https://api.github.com/users/{username}")
    response = requests.get(url)
    if response.status_code == 200:
        user_data = response.json()
        user_name = user_data["login"]
        name = user_data["name"]
        bio = user_data["bio"]
        followers = user_data["followers"]
        following = user_data["following"]
        repositories = user_data["public_repos"]
        html_url = user_data["html_url"]\

        user_list.append(user_data)

        with open("github_username.json", "w") as file:
            json.dump(user_list, file, indent=4)

        listbox.insert(tk.END, f"Username: {user_name}")
        listbox.insert(tk.END, f"Name: {name}")
        listbox.insert(tk.END, f"Bio: {bio}")
        listbox.insert(tk.END, f"Followers: {followers}")
        listbox.insert(tk.END, f"Following: {following}")
        listbox.insert(tk.END, f"Repositories: {repositories}")
        listbox.insert(tk.END, f"Profile URL: {html_url}")

        entry1.delete(0, tk.END)

    elif response.status_code == 404:
        results.config(text="Result: User not found")

    elif response.status_code == 500:
        results.config(text="Result: Server error")

with open("github_username.json", "r") as file:
    user_data2 = json.load(file)

button = tk.Button(window, text="Search", command=program)
button.pack()

window.mainloop()


