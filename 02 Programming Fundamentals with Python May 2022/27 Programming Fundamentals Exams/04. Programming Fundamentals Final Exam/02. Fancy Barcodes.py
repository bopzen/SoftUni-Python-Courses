import re
n = int(input())
search_pattern = r"(@#+)([A-Z][A-Za-z0-9]{4}[A-Za-z0-9]*[A-Z])(@#+)"
search_pattern_digits = r"\d*"

for _ in range(n):
    barcode = input()
    result = re.search(search_pattern, barcode)
    if result:
        product = result.group(2)
        product_code = ""
        product_code_list = re.findall(search_pattern_digits, product)
        for digit in product_code_list:
            product_code += digit
        if product_code == "":
            print("Product group: 00")
        else:
            print(f"Product group: {product_code}")
    else:
        print("Invalid barcode")

