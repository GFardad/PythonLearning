list_Moz = [
    "North",
    "West",
    "North",
    "South",
    "East",
    "East",
    "West",
    "North",
    "South",
    "South",
    "South",
]
Result = []

for i in range(1, len(list_Moz)):
    if list_Moz[i] == "North":
        if list_Moz[i - 1] != "South":
            Result.append(list_Moz[i])
            print("N")
        else:
            Result.pop()

    if list_Moz[i] == "West":
        if list_Moz[i - 1] != "East":
            Result.append(list_Moz[i])
            print("W")
        else:
            Result.pop()
    if list_Moz[i] == "South":
        if list_Moz[i - 1] != "North":
            Result.append(list_Moz[i])
            print("S")
        else:
            Result.pop()
    if list_Moz[i] == "East":
        if list_Moz[i - 1] != "West":
            Result.append(list_Moz[i])
            print("E")
        else:
            Result.pop()
print(Result)
