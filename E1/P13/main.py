input_list = [1, 10, 11, 12, 20, 21, 22, 30]

result = []
z = 1
for i in range(len(input_list) - 1):

    curent_val = input_list[i]
    pre_val = input_list[i - 1]
    next_val = input_list[i + 1]

    if (curent_val + 1) == (next_val):
        z += 1

    else:

        z = 0

    if z == 3:
        result.append(curent_val)
        z = 1
print(result)