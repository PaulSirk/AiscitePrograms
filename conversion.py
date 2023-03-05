money = {
        "penny": 0.01,
        "nickel": 0.05,
        "dime": 0.1,
        "quarter": 0.25,
        "one": 1.0,
        "two": 2.0,
        "five": 5.0,
        "ten": 10.0,
        "twenty": 20.0,
        "fifty": 50.0,
        "hundred": 100
        }

conversion: float = 0.0

firstNum = input("What kind of coin or bill do you have? ").lower()
secondNum = input("\nWhat do you want to convert it to? ").lower()

conversion = round(money[firstNum]/money[secondNum], 2)

if secondNum == "penny" or secondNum == "twenty" or secondNum == "fifty":
	secondNum = secondNum[:-1] + "ies"
else:
	secondNum += "s"

print(f"You have {conversion} {secondNum}.")
