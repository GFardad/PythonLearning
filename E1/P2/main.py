def shomarande(list_items):
    meghdar = {}
    for item in list_items:
        if item in meghdar:
            meghdar[item] += 1
        else:
            meghdar[item] = 1
    return meghdar


def sound_remover(inp_str):
    sound = "aeiouy"
    result = []
    for char in inp_str:
        if char not in sound:
            result.append(char)
    return "".join(result)


input_string = input("Moz : ")
print(sound_remover(input_string))


shomaresh = shomarande(input_string)


print("--------")


for char, count in sorted(shomaresh.items(), key=lambda item: item[1], reverse=True):
    print(f"harf: {char}, tekrar: {count}")
