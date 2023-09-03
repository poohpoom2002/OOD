def generate_binary(num, current = ""):
    if num < 0:
        print("Only Positive & Zero Number ! ! !")
    elif num == 0 :
        if current == "":
            print("0")
        else:
            print(current)
    else:
        generate_binary(num - 1, current + "0")
        generate_binary(num - 1, current + "1")

num = int(input("Enter Number : "))
generate_binary(num)