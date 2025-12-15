def fillera(n):
    if n <= 0:
        n = 0
    mul = 0
    mazareb = []
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            mazareb.append(i)
    for i in range(len(mazareb)):
        mul = mazareb[i] + mul

    return mul


userInp = int(input("Give me a number : "))
result = fillera(userInp)
print(result)
