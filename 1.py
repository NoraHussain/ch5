total = 0
try:
    while total <= 50:
        x = int(input("Enter number: "))
        total += x
        print("total = ", total)

    print("loop finished")
    print("total = ", total)

except:
    print("Not num !")
