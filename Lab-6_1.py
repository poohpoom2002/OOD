def fibonacci(num):
    if num == 1 or num == 2:
        return 1
    return fibonacci(num - 1) + fibonacci(num - 2)

num = int(input("Enter Number : "))
print(f"fibo({num}) = {fibonacci(num)}")