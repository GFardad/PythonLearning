a_list = ["A", "B", "C", "D"]
b_list = ["B", "C"]
result = []
i = 0

for a_item in a_list:
    found_in_b = False
    for b_item in b_list:
        if a_item == b_item:
            found_in_b = True
            break
    if not found_in_b:
        result.append(a_item)


print(result)


a_list = ["A", "B", "C", "D"]
b_list = ["B", "C"]
result = (set(a_list)) - (set(b_list))
print(sorted(result))
