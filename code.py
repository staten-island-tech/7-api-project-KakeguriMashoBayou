
import tkinter as tk
import requests
from PIL import Image, ImageTk


def pet_axolotl():
    global photo
    url = "https://theaxolotlapi.netlify.app/"
    response = requests.get(url)
    with open("axolotl.jpg", "wb") as f:
        f.write(response.content)
    image = Image.open("axolotl.jpg")
    photo = ImageTk.PhotoImage(image)
    label.config(image=photo)
    label.image = photo

window = tk.Tk()
window.title("Axolotls")
window.geometry("1200x800")
window.resizeable(False, False)
prompt = tk.Label(window,text = "Click the button for an axolotl",font = ("Arial, 16"))
prompt.pack(pady = 10)

button = tk.Button( window, text = "Axolotl", command = pet_axolotl, font = ("Arial", 16), bg = "pink", fg = "blue")
button.pack(pady = 20)
label = tk.Label(window)
label.pack(pady=30)
window.mainloop()