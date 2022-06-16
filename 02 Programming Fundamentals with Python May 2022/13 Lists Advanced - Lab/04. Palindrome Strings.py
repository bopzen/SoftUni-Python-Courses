list_words = input().split()
palindrome = input()
list_palindrome = []
for element in list_words:
    if element == "".join(reversed(element)):
        list_palindrome.append(element)
print(list_palindrome)
print(f"Found palindrome {list_words.count(palindrome)} times")