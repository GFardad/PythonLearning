def zarb(x):
    x = str(x)
    if (len(x)==1):
        return(x)
    else :
        x_list = []
        for i in range(len(x)):
            x_list.append(x[i])

        for i in range(len(x) - 1):
            z = int(x_list[i]) * int(x_list[i + 1])
    return zarb(z)


result = zarb(45)
print(result)