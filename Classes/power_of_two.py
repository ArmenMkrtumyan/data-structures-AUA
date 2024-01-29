def recursive(n):
    if n == 1:
        return 1
    if n < 1:
        return 0
    return recursive(n / 2)


while True:
    try:
        number = int(input("Input an integer: "))
        if number > 1 and recursive(number):
            print("Power of two")
        else:
            print("Not a power of two")
    except ValueError:
        print("INPUT AN INTEGER")
