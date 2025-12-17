def sum_of_dijets(x):
    if len(str(x)) == 1:
        return x
    # y = 0
    x_list = [int(x)[i] for i in range(len(str(j))),j]
    print(x_list)
    # x_intl = [int(x)[i] for i in range(len(str(x)))]
    x = sum(x_list)
    if len(str(x)) == 1:
        return x


inpUser = int(input("Give me a number : "))
print(sum_of_dijets(inpUser))
