start_1st_pair = int(input())
start_2nd_pair = int(input())
diff_end_1st_pair = int(input())
diff_end_2nd_pair = int(input())
end_1st_pair = start_1st_pair + diff_end_1st_pair
end_2nd_pair = start_2nd_pair + diff_end_2nd_pair

for pair1 in range(start_1st_pair, end_1st_pair+1):
    for pair2 in range(start_2nd_pair, end_2nd_pair+1):
        is_pair1_prime = True
        is_pair2_prime = True
        for p1 in range(2,pair1):
            if pair1 % p1 == 0:
                is_pair1_prime = False
                break
        for p2 in range(2,pair2):
            if pair2 % p2 == 0:
                is_pair2_prime = False
                break
        if is_pair1_prime and is_pair2_prime:
            print(pair1,pair2,sep='')