number = int(input("Enter Input : "))
for i in range(2 * number + 4) :
    for j in range(2 * number + 4) :
        if i + j <= number or (2 * number + 3 - i) + (2 * number + 3 - j) <= number :
            print(".", end = "")
        elif j < number + 2 and not (2 * number + 3 > i > number + 2 and number + 1 > j > 0) or number + 1 > i > 0 and 2 * number + 3 > j > number + 2 :
            print("#", end = "")
        else :
            print("+", end = "")
    print("")