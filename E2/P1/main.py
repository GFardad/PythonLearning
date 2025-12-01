def fillera(n, *a):
    if n < 0:

        if len(a) == 0:
            return 0
        else:
            not_valid_inp = "not valid input, pls enter non negative intiger", 0
            return not_valid_inp

    basemazrab = []
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            basemazrab.append(i)

    if len(a) == 0:
        return sum(basemazrab)
    else:
        return sum(basemazrab), basemazrab


result = fillera(10, 1)
if type(result) == int:
    print(result)
else:
    print(f" Sum is : {result[0]}, List is : {result[1]}") # type: ignore
