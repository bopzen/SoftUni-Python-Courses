str1, str2 = input().split()
total = 0
if len(str1) > len(str2):
    for i in range(len(str2)):
        total += ord(str2[i])*ord(str1[i])
    for i in range(len(str2),len(str1)):
        total += ord(str1[i])
elif len(str2) > len(str1):
    for i in range(len(str1)):
        total += ord(str2[i])*ord(str1[i])
    for i in range(len(str1),len(str2)):
        total += ord(str2[i])
else:
    for i in range(len(str1)):
        total += ord(str2[i])*ord(str1[i])
print(total)