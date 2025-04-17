amount_due = 50
running_payment = 0


def get_coin():
    while True:
        print(f"Amount Due: {amount_due}")
        payment = int(input("Insert Coin: "))
        if payment == 5 or payment == 10 or payment == 25:
            return payment


while amount_due > 0:
    payment = get_coin()
    amount_due = amount_due - payment
    running_payment = running_payment + payment


change = abs(50 - running_payment)


print(f"Change Owed: {change}")

