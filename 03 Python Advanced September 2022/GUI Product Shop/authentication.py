from json import loads, dump
from buying_page import display_products
from canvas import *
from helpers import clean_screen


def render_entry():
    register_btn = tk.Button(
        root,
        text="Register",
        bg="green",
        fg='white',
        borderwidth=0,
        width=20,
        height=3,
        command=register
    )

    login_btn = tk.Button(
        root,
        text="Login",
        bg="Blue",
        fg='white',
        borderwidth=0,
        width=20,
        height=3,
        command=login
    )

    frame.create_window(350, 250, window=register_btn)
    frame.create_window(350, 310, window=login_btn)


def login():
    clean_screen()
    frame.create_text(250, 160, text="Username", anchor='w')
    frame.create_text(250, 190, text="Password", anchor='w')

    frame.create_window(380, 160, window=username_box)
    frame.create_window(380, 190, window=password_box)

    logging_btn = tk.Button(
        root,
        text="Login",
        bg="Blue",
        fg='white',
        borderwidth=0,
        width=20,
        height=3,
        command=logging
    )

    frame.create_window(350, 410, window=logging_btn)


def logging():
    if check_login():
        display_products()
    else:
        frame.create_text(
            350,
            300,
            text="Invalid username or password!",
            fill="red",
            tag='error'
            )


def check_login():
    users_data = get_users_data()
    for record in users_data:
        if record['username'] == username_box.get() and record['password'] == password_box.get():
            return True

    return False


def register():
    clean_screen()

    frame.create_text(250, 100, text="First Name", anchor='w')
    frame.create_text(250, 130, text="Last Name", anchor='w')
    frame.create_text(250, 160, text="Username", anchor='w')
    frame.create_text(250, 190, text="Password", anchor='w')

    frame.create_window(380, 100, window=first_name_box)
    frame.create_window(380, 130, window=last_name_box)
    frame.create_window(380, 160, window=username_box)
    frame.create_window(380, 190, window=password_box)

    registration_btn = tk.Button(
        root,
        text="Register",
        bg="green",
        fg='white',
        borderwidth=0,
        width=20,
        height=3,
        command=registration
    )

    frame.create_window(350, 410, window=registration_btn)


def registration():
    new_credentials = {
        "first_name": first_name_box.get(),
        "last_name": last_name_box.get(),
        "username": username_box.get(),
        "password": password_box.get(),
        "products": []
    }
    if check_registration(new_credentials):
        with open("db/user_information.json", "a") as users_file:
            dump(new_credentials, users_file)
            users_file.write('\n')


def check_registration(credentials):
    if credentials['first_name'].strip() == "" \
            or credentials['last_name'].strip() == "" \
            or credentials['username'].strip() == "" \
            or credentials['password'].strip() == "":
        frame.create_text(
            350,
            300,
            text="Please fill out all fields",
            fill="red",
            tag='error'
        )
        return False
    frame.delete('error')
    users_data = get_users_data()
    for record in users_data:
        if record['username'] == credentials['username']:
            frame.create_text(
                350,
                300,
                text="Username already exists!",
                fill="red",
                tag='error'
            )
            return False
    frame.delete('error')
    return True


def get_users_data():
    users_data = []
    with open("db/user_information.json", "r") as users_file:
        for line in users_file:
            users_data.append(loads(line))
    return users_data


first_name_box = tk.Entry(root, bd=0)
last_name_box = tk.Entry(root, bd=0)
username_box = tk.Entry(root, bd=0)
password_box = tk.Entry(root, bd=0, show="*")
