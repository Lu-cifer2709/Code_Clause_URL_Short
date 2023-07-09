import pyshorteners
import tkinter as tk

def shurl():
    url = url_entry.get()
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(url)
    short_url_label.configure(text=short_url)
    print("The short Url of Given url is :")
    print(short_url)

root = tk.Tk()
root.title("URL Shortener")

url_label = tk.Label(root, text="Enter URL:")
url_label.pack()

url_entry = tk.Entry(root, width=50)
url_entry.pack()

shorten_button = tk.Button(root, text="Shorten", command=shurl)
shorten_button.pack()

short_url_label = tk.Label(root, text="")
short_url_label.pack()

root.mainloop()


