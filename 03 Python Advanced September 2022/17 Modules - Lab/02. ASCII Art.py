from pyfiglet import figlet_format


def print_art(msg):
    art_message = figlet_format(msg)
    print(art_message)

message = input('What would you like to print? ')
print_art(message)