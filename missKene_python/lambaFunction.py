# product = lambda x,y:x*y
# print("Product of 4, 5 =", product(4,5))

numbers = [1, 2, 3, 4]
result = list(map(lambda x:x*2, numbers))
for res in result:
    print(res)