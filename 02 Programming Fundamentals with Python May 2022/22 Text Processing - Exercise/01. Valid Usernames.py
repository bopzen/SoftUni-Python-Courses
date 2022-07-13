usernames = input().split(", ")
for word in usernames:
    not_valid = False
    if 3 <= len(word) <= 16:
        for ch in word:
            if ch.isalnum() or ch in '_-':
                continue
            else:
                not_valid = True
                break
    else:
        not_valid = True
    if not not_valid:
        print(word)