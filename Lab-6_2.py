def wrapper_trade(wrapper, wrap):
    if wrapper < wrap:
        return 0
    return wrapper//wrap + wrapper_trade((wrapper//wrap) + (wrapper%wrap), wrap)

money, price, wrap = [int(x) for x in input("Enter m, p, w: ").split(" ")]
print(int(money//price + wrapper_trade(money//price, wrap)))