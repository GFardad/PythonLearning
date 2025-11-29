a_list = ["A", "B", "C", "D"]
b_list = ["B", "C"]
result = []

# print((len(a_list)))

for a_item in a_list:
    found_in_b = False
        for b_item in b_list:
            if a_item == b_item:
                result.append(a_item)
        else:
            i += 1
print(result)
