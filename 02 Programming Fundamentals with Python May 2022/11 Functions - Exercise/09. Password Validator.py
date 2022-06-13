def check_password(password):
    has_invalid_char = False
    is_too_long = False
    count_num = 0
    if len(password) > 10 or len(password) < 6:
        is_too_long = True
        print("Password must be between 6 and 10 characters")
    for element in password:
        if 48 <= ord(element) <= 57 or 65 <= ord(element) <= 90 or 97 <= ord(element) <= 122:
            if 48 <= ord(element) <= 57:
                count_num += 1
        else:
            has_invalid_char = True
    if has_invalid_char:
        print("Password must consist only of letters and digits")
    if count_num < 2:
        print("Password must have at least 2 digits")
    if not has_invalid_char and not is_too_long and count_num >= 2:
        print("Password is valid")


check_password(input())