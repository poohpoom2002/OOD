print("*** String Rotation ***")
string_1, string_2 = [x for x in input("Enter 2 strings : ").split()]
temp_1 = string_1
temp_2 = string_2
count = 0
while True :
    temp_1 = temp_1[-2] + temp_1[-1] + temp_1
    temp_1 = temp_1[:-2]
    temp_2 = temp_2 + temp_2[0] + temp_2[1] + temp_2[2]
    temp_2 = temp_2[3:]
    count += 1
    if count <= 5 or temp_1 == string_1 and temp_2 == string_2 :
        print(count, temp_1, temp_2)
    elif count == 6 :
        print(" . . . . . ")
    if temp_1 == string_1 and temp_2 == string_2 :
        break
print(f"Total of  {count} rounds.")