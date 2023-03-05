import locale

money = {
        "pennies" : 0.01,
        "nickels": 0.05,
        "dimes": 0.1,
        "quarters": 0.25,
        "ones": 1.0,
        "twos": 2.0,
        "fives": 5.0,
        "tens": 10.0,
        "twenties": 20.0,
        "fifties": 50.0,
        "hundreds": 100.0
        }

sum : float = 0

for key in money:
    amount = float(input("How many {0} do you have? ".format(key)))
    sum += amount * money[key]

locale.setlocale(locale.LC_ALL, '')
money = locale.currency(sum, grouping=True)

print("You have {0}.".format(money))
