def sum_of_dijets(x):
    y = 0
    x_list = []
    if len(str(x)) == 1:
        return x

    map(lambda d: x_list.append(str(x)[d]), range(len(str(x))))
    # print(x_list)
    x = sum(x_list)
    if len(str(x)) == 1:
        return x
    else:
        # y+=1
        sum_of_dijets(x)


inpUser = int(input("Give me a number : "))
print(sum_of_dijets(inpUser))
