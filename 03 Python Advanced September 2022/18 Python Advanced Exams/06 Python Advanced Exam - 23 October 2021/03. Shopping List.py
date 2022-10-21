def shopping_list(budget, **products):
    if budget < 100:
        return "You do not have enough budget."

    basket = 0
    result = []
    for product, price_quantity in products.items():
        price, quantity = price_quantity[0], price_quantity[1]
        total = price * quantity
        if budget >= total:
            result.append(f"You bought {product} for {total:.2f} leva.")
            budget -= total
            basket += 1
        if basket == 5:
            break

    return '\n'.join(result)