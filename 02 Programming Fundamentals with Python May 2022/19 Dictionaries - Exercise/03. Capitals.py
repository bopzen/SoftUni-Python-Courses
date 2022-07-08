list_country = input().split(", ")
list_capital = input().split(", ")

dict_country_capital = {key: value for key, value in zip(list_country, list_capital)}

print("\n".join(f"{key} -> {value}" for key, value in dict_country_capital.items()))