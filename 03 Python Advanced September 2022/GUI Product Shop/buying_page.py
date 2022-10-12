from json import load
from helpers import clean_screen
from PIL import Image, ImageTk
from canvas import *


def display_products():
    clean_screen()
    display_stock()


def display_stock():
    with open("db/products_data.json", "r") as products_file:
        products_info = load(products_file)

    x, y = 150, 50

    for name, info in products_info.items():
        product_img = ImageTk.PhotoImage(Image.open(products_info['name']['image']))
        frame.create_text(x, y, text=name)
        frame.create_image(x, y + 100, image=product_img)