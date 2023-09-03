def mod_position(arr, s):
    return [arr[i] for i in range(len(arr)) if (i + 1) % int(s) == 0]

print("*** Mod Position ***")
message, num = input("Enter Input : ").split(",")
print(mod_position(message, num))