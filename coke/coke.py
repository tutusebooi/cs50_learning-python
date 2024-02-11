amount = 0
total_amount = 50
coin_accept = [25, 10, 5]

print("Amount Due: 50")
while amount != total_amount:
    insert_coin = int(input("Insert Coin: "))
    if insert_coin in coin_accept:
        amount += insert_coin
    else:
        print("Amount Due: 50")
        continue

    if amount < total_amount:
        print(f"Amount Due: {total_amount - amount}")
    elif amount > total_amount:
        print(f"Change Owed: {amount - total_amount}")
        break
else:
    print("Change Owed: 0")
