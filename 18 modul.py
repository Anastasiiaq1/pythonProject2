count_bilet = int(input("Введите количество билетов:"))
price = 0
for i in range(count_bilet):
    age = int(input("Введите возраст:"))
    if age < 18:
        price += 0
    if 18 <= age < 25:
        price += 990
    if age >= 25:
        price += 1390
if count_bilet > 3:
    price = int(price - (price * 0.1))
print(f"Итог:{price}")