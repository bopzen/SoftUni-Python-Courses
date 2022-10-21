from collections import deque

flowers = {
    'rose': set('rose'),
    'tulip': set('tulip'),
    'lotus': set('lotus'),
    'daffodil': set('daffodil')
}

vowels = deque(input().split())
consonants = input().split()
word_found = False
while vowels and consonants:
    vowel = vowels.popleft()
    consonant = consonants.pop()
    for key, value in flowers.items():
        if vowel in value:
            value.remove(vowel)
        if consonant in value:
            value.remove(consonant)
        if len(value) == 0:
            print(f"Word found: {key}")
            word_found = True
            break
    if word_found:
        break
else:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")