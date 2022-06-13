def palindrome(list_numbers):
    for element in list_numbers:
        is_palindrome = None
        if len(element) == 1:
            is_palindrome = True
        else:
            for i in range(len(element)//2):
                if element[i] != element[-(i+1)]:
                    is_palindrome = False
                    break
                else: is_palindrome = True
        print(is_palindrome)


numbers = input().split(", ")
palindrome(numbers)