def bon(w):
    for i in range(len(w) - 1):
        for j in range(i + 1, len(w)):
            if w[i] == w[j]:
                return (ord(w[j]) - 96) * 4

secretCode = input("Enter secret code : ")
print(bon(secretCode))