def colats_core(x):
    xl = x
    i = 0

    while xl != 1:
        if xl % 2 == 1:
            xl = xl * 3 + 1
            print(xl)
        elif xl % 2 == 0:
            xl = xl // 2
            print(xl)
        i += 1
    return xl, i


def main():
    x = int(input("Give number : "))
    xl, i = colats_core(x)
    printo(xl, i)


def printo(xl, i):

    print("-" * 10)
    print(f"Finish {xl} done in {i} step")


if __name__ == "__main__":
    main()
