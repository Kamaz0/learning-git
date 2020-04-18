zakupy = {
    "piekarnia": ["chleb", "bułki", "pączek"],
    "warzywniak": ["marchew", "seler", "rukola"]}

# ręcznie
# print(f"Pierwsza jest {[key for key in zakupy.keys()][0]}, kupuję tu następujące rzeczy: {[value for value in zakupy.values()][0]}")
# print(f"Pierwsza jest {[key for key in zakupy.keys()][1]}, kupuję tu następujące rzeczy: {[value for value in zakupy.values()][1]}")

# capital_letters
# name = "cokolwiek"
# print(name.capitalize())

# capital_letters in list
# str2 = [towar.capitalize() for towar in lista]

#automatycznie, len(zakupy) liczy ilość par, czyli klucz-wartość
for e in range(len(zakupy)):
    print(f"Pierwsza jest {([key for key in zakupy.keys()][e])}, kupuję tu następujące rzeczy: {[value for value in zakupy.values()][e]}")

#automatycznie_proper
for sklep, lista in zakupy.items():
   str2 = [towar.capitalize() for towar in lista]
   print(f"Pierwsza jest {sklep.capitalize()}, kupuję tu następujące rzeczy: {str2}")

ctr = sum(map(len, zakupy.values()))
print(f"W sumie kupuję {ctr} produktów")

# print(zakupy) # to wyświetla cały słownik
# print(zakupy["piekarnia"]) # to wyświetla wszystkie wartości klucza1
# print(zakupy.items()) #prints keys and values
# print(zakupy.keys()) #prints keys
# print(zakupy.values()) #prints values

print("There is no dick in the village!")
print("Enough of this BS!")
