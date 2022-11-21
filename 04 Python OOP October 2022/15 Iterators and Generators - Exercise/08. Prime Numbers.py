def get_primes(integers):
    for num in integers:
        if num <= 1:
            continue
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            yield num