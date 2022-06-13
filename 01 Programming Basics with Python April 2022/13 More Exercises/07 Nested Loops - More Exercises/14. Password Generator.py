n = int(input())
L = int(input())
for symbol1 in range(1, n+1):
    for symbol2 in range(1, n+1):
        for symbol3 in range(97, 97+L):
            for symbol4 in range(97, 97+L):
                for symbol5 in range(max(symbol1,symbol2)+1, n+1):
                    print(f"{symbol1}{symbol2}{chr(symbol3)}{chr(symbol4)}{symbol5}", end=' ')