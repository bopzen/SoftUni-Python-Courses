list_cards = input().split()
count_shuffle = int(input())
for shuffles in range(count_shuffle):
    final_deck = []
    middle = len(list_cards) // 2
    left_deck = list_cards[0:middle]
    right_deck = list_cards[middle::]
    for index in range(len(left_deck)):
        final_deck.append(left_deck[index])
        final_deck.append(right_deck[index])
    list_cards = final_deck
print(list_cards)