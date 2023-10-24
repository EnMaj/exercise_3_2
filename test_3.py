def final_price(cost, card, day):
    sale = 0
    if card:
        sale += 5
    elif day:
        sale += 3
    elif 5000 < cost < 15000:
        sale += 3
    elif 15000 < cost < 20000:
        sale += 5
    elif 20000 < cost < 30000:
        sale += 7
    elif cost > 30000:
        sale += 10
    if sale > 15:
        sale = 15
    return "%.2f" % (cost - (cost/100)*sale)

cost = float(input("Введите цену: "))
card = bool(input("Вы обладаете дисконтной картой? "))
day = bool(input("Сегодня праздничный день? "))
print(final_price(cost, card, day))
