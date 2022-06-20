list_text = input().split()
list_even = [text for text in list_text if len(text) % 2 == 0]
print("\n".join(map(str, list_even)))