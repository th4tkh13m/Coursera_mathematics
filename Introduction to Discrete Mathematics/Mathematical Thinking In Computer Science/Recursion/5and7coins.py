def change(amount):
    if amount == 10:
        return [5, 5]
    if amount == 5:
        return [5]
    if amount == 25:
        return [5, 5, 5, 5, 5]
    if amount == 15:
        return [5, 5, 5]
    if amount == 20:
        return [5, 5, 5, 5]
    if amount == 30:
        return [5, 5, 5, 5, 5, 5]
    if amount == 0:
        return []


    coin = change(amount - 7)
    coin.append(7)
    return coin

# complete this method
for i in range(24, 30):
    print(change(i))
