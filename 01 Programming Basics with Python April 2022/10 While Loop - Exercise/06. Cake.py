width = int(input())
length = int(input())
num_pieces = width * length
while num_pieces >0:
    pieces_taken = input()
    if pieces_taken == 'STOP':
        print(f'{num_pieces} pieces are left.')
        break
    pieces_taken = int(pieces_taken)
    num_pieces -= pieces_taken
if num_pieces<=0:
    print(f"No more cake left! You need {abs(num_pieces)} pieces more.")