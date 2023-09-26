def linear_search_product(product_list, target_product):
    indices = []
    
    for i in range(len(product_list)):
        if product_list[i] == target_product:
            indices.append(i)
    
    return indices

products = ["apple", "banana", "orange", "apple", "apple", "banana", "lemon"]
target = "apple"
result = linear_search_product(products, target)
print(result)