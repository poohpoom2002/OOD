class MyInt:
    def toRoman(self, num):
        roman_numerals = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I"
        }
        roman = ""
        for value, symbol in roman_numerals.items():
            while num >= value:
                roman += symbol
                num -= value
        return roman

    def add(self, num1, num2):
        result = int((num1 + num2) * 1.5)
        return result

print(" *** class MyInt ***")
my_int = MyInt()
num1, num2 = input("Enter 2 number : ").split()
num1, num2 = int(num1), int(num2)
print(f"{num1} convert to Roman : {my_int.toRoman(num1)}")
print(f"{num2} convert to Roman : {my_int.toRoman(num2)}")
print(f"{num1} + {num2} = {my_int.add(num1, num2)}")