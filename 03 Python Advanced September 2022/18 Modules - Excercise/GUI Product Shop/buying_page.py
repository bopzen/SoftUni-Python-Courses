from json import load, dump
from tkinter import Button

from helpers import clean_screen
from PIL import Image, ImageTk
from canvas import *


def display_products():
    clean_screen()
    display_stock()


def display_stock():
    global products_info

    with open("db/products_data.json", "r") as products_file:
        products_info = load(products_file)

    x, y = 120, 70

    for name, info in products_info.items():
        image = Image.open(info['image'])
        image = image.resize((130, 130))
        product_img = ImageTk.PhotoImage(image)
        images.append(product_img)
        frame.create_text(x, y, text=name)
        frame.create_image(x, y + 80, image=product_img)
        if info['quantity'] > 0:
            color="green"
            text = f"In stock {info['quantity']}"
            buy_btn = Button(
                root,
                text='Buy',
                bg='green',
                fg='white',
                width=5,
                borderwidth=0,
                command=lambda name=name: buy_product(name)
            )
            frame.create_window(x, y + 190, window=buy_btn)
        else:
            color = "red"
            text = "Out of stock"
        frame.create_text(x, y + 160, text=text, fill=color)

        x += 150
        if x > 600:
            x = 120
            y += 270


def buy_product(product):
    products_info[product]['quantity'] -= 1
    with open("db/products_data.json", "w") as products_file:
        dump(products_info, products_file)

    display_products()


images = []