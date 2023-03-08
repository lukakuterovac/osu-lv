while True:
    try:
        num = float(input("Number: "))
        while num > 1 or num < 0:
            print("Outside of range")
            num = float(input("Number: "))
        if num <= 1.0 and num >= 0.9:
            print("A")
            break
        elif num >= 0.8:
            print("B")
            break
        elif num >= 0.7:
            print("C")
            break
        elif num >= 0.6:
            print("D")
            break
        elif num >= 0.0:
            print("F")
            break
    except ValueError:
        print("Enter a number")
