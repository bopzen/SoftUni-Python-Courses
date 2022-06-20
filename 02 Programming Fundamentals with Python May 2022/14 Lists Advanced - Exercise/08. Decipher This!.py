list_words = input().split()

for word in list_words:
    num = "".join(filter(lambda x: x.isdigit(), word))
    ch = "".join(filter(lambda x: not x.isdigit(), word))
    num = chr(int(num))
    list_ch = [c for c in ch]
    list_ch[0], list_ch[-1] = list_ch[-1], list_ch[0]
    print(num + "".join(list_ch), end=' ')