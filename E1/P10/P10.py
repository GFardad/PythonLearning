def validator(n):
    abs_number = abs(n)
    if n < 0:
        print(f"[ {n} ] is less then 0 \nbut we calc for {abs_number}")
    return abs_number


def calc_sum(number, k):
    m = (number - 1) // k
    final_sum = ((k + k * m) * m) // 2
    array_mk = []
    for i in range(0, number, k):
        if i <= number:
            array_mk.insert(0, i)

    return final_sum, array_mk


memory = []
for_array = [3, 5, 15]
input_number = int(input("Give me a number : "))
valid_number = validator(input_number)
i = 0
for base in for_array:
    final_sum, array_mk = calc_sum(valid_number, for_array[i])
    print("-" * 30)
    print(f"For [ {valid_number} ] arrau is {array_mk} and a sum ofthem is {final_sum}")
    memory.insert(i, final_sum)
    i += 1
mul_sum = memory[0] + memory[1] - memory[2]
print(f"{memory} \n Final sum is : {mul_sum}")
