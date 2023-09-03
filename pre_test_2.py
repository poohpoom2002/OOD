print(' *** Divisible number ***')
x = int(input("Enter a positive number : "))
if x <= 0 :
    print(x, "is OUT of range !!!")
else :
    count = 0
    print("Output ==> ", end = '')
    for i in range(1, x+1) :
        if x % i == 0 :
            print(i ,end = ' ')
            if i == x :
                print('')
            count += 1
    print("Total ==>", count)