basemazrab = []
def fillera(n):
    for i in range(n):
        if i%3 == 0 or i%5 == 0:
            basemazrab.append(n)

    return basemazrab


def mazrabyab(n):
    for i in range(n):
        

print(fillera(4))