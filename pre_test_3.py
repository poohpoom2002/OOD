print(' *** String count ***')
massage = input("Enter message : ")
upper = 0
lower = 0
uppercase = []
lowercase = []
for x in massage :
    if ord(x) <= 90 and ord(x) >= 65 :
        upper += 1
        for i in range(len(uppercase)) :
            if x == uppercase[i] :
                break
            if i == len(uppercase) - 1 :
                uppercase.append(x)
        if len(uppercase) == 0 :
            uppercase.append(x)
    elif ord(x) <= 122 and ord(x) >= 97 :
        lower += 1
        for i in range(len(lowercase)) :
            if x == lowercase[i] :
                break
            if i == len(lowercase) - 1 :
                lowercase.append(x)
        if len(lowercase) == 0 :
            lowercase.append(x)
uppercase.sort()
lowercase.sort()
print("No. of Upper case characters :", upper)
print("Unique Upper case characters : ", end = '')
if len(uppercase) == 0 :
    print('')
else :
    for i in range(len(uppercase)) :
        print(uppercase[i], end = '  ')
        if i == len(uppercase) - 1 :
            print('')
print("No. of Lower case Characters :", lower)
print("Unique Lower case characters : ", end = '')
if len(lowercase) == 0 :
    print('')
else :
    for i in range(len(lowercase)) :
        print(lowercase[i], end = '  ')
        if i == len(lowercase) - 1 :
            print('')