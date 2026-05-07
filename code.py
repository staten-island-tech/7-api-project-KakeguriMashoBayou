import tkinter as tk
import requests
from PIL import Image, ImageTk


def pet_axolotl():
    global photo
    url = 'https://theaxolotlapi.netlify.app/'
    response = requests.get(url)
    with open("axolotl.png", "wb") as f:
        f.write(response.content)

