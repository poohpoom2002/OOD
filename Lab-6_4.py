def find_product_combinations(money, products,results,current_combination = []):
    if money == 0:
        results.append(current_combination)
        return

    if money < 0 or len(products) == 0:
        return

    # Include the current product in the combination
    find_product_combinations(money - products[0], products[1:], results, current_combination + [products[0]])

    # Exclude the current product from the combination
    find_product_combinations(money, products[1:], results, current_combination)

def print_combinations(results, index = 0):
    if index < len(results):
        print(" ".join(map(str, results[index])))
        print_combinations(results,index + 1)

def change_to_int(lst, index= 0):
    if index == len(lst):
        return []
    else:
        return [int(lst[index])] + change_to_int(lst,index + 1)
    
money,products = input('Enter Input (Money, Product) : ').split('/')    
money = int(money)
products = change_to_int(products.split(' '))
results = []

find_product_combinations(money, products,results)
print_combinations(results)
print(f"Krisada can purchase Product: {products} with: {money} Baht | {len(results)} Pattern")