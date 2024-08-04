from random import randint

def advantage_bot():
    sum = 0

    print("----------------------\n")
    d = int(input("Dice sides = "))
    print("")
    itterations = int(input("Itterations = "))
    print("\n----------------------\n")

    i = 0
    for i in range(1,itterations + 1):
        a = randint(1,d)
        b = randint(1,d)
        if a >= b: sum += a
        else: sum += b

    print(f"Calculated average = {sum / itterations}\n")
    print(f"AnyDice average = 13.82\n")
    print("----------------------")

advantage_bot()
