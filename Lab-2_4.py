def sum_five(arr):
    if len(arr) < 3:
        return "Array Input Length Must More Than 2"
    arr.sort()
    ans = []
    for i in range(len(arr) - 2):
        for j in range(i + 1, len(arr) - 1):
            for k in range(j + 1, len(arr)):
                if arr[i] + arr[j] + arr[k] == 5:
                    if ans == []:
                        ans.append([arr[i], arr[j], arr[k]])
                    else:
                        for x in ans:
                            if x == [arr[i], arr[j], arr[k]]:
                                break
                            ans.append([arr[i], arr[j], arr[k]])
    return ans

lst = [int(x) for x in input("Enter Your List : ").split(" ")]
print(sum_five(lst))