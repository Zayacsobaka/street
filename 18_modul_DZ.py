sum_tickets = 0
qnt_tickets = int(input("Введите количество билетов: "))
for age in range(qnt_tickets):
    age = int(input("Введите возраст посетителя: "))
    if age < 18:
        sum_tickets += 0
    elif 18 <= age <=25:
        sum_tickets += 990
    elif age > 25:
        sum_tickets += 1390
print("Стоимость Ваших билетов: ", sum_tickets)
if qnt_tickets > 3:
    print("Сумма с учетом скидки: ", sum_tickets - ((sum_tickets / 100) * 10))

