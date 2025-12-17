"""
Docstring for E2.P2.main
این تابع قرار است "Digital Root" یا همان ریشه رقمی عدد را حساب کند
"""


def sum_of_digits(x: int, step=0):
    total = 0
    if x < 10:
        return x, step
    while x > 0:
        x, y = divmod(x, 10)
        total = total + y
    step += 1
    return sum_of_digits(total, step)


inp_user = abs(int(input("Give me a number : ")))
total_sum, step = sum_of_digits(inp_user)
print(f"{total_sum} is {inp_user} diget sum \n calced in {step} steps")
