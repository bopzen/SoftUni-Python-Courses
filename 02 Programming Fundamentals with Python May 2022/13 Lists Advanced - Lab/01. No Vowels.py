list_vowels = ['a', 'o', 'u', 'e', 'i']

text = input()
print("".join(char for char in text if char.lower() not in list_vowels))