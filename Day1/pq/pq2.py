# . Filter Expensive Products
# Select products costing more than 500.

products=[('Laptop',70000),('Mobil',20000),('Tablet',100000),('Headphones',500),('Charger',300),('Camera',60000)]

def sort_by_3000(products):
    exp_prod=[]
    
    for p in products:
        if p[1] > 3000:
            exp_prod.append(p)
    return exp_prod


#  if we also consider the length of alphabet in the product name then we can use the below code

def sort_by_alp(products):
    
    for i in range(len(products)):
        for j in range(len(products)-i-1):

            if len(products[i][0]) > len(products[i+1][0]) and products[i][1] > 3000:
                products[j], products[j + 1] = products[j + 1], products[j]

    return products
print(sort_by_alp(products))
