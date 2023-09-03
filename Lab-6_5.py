def permute_string(s, k):
    if k < 0:
        return "Invalid value of k. k must be a non-negative integer."
    if k > len(s):
        return "Invalid value of k. k must be less than or equal to the length of the string."
    if k == 0:
        return ['']
    
    def generate_permutations(s, start, end, k):
        if start == end:
            result.append(''.join(s[:k]))
        else:
            for i in range(start, end + 1):
                s[start], s[i] = s[i], s[start]
                generate_permutations(s, start + 1, end, k)
                s[start], s[i] = s[i], s[start]
    
    result = []
    generate_permutations(list(s), 0, len(s) - 1, k)
    result = list(dict.fromkeys(result))
    result.sort()
    return result

input_string, k = input("Enter a string and k: ").split("/")
permutations = permute_string(input_string, int(k))
print(permutations)