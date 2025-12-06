Fn = [0,1]
def moz(inputint):
    # for i in range(2, inputint):
        Fn[i] = moz(i-1) + moz(i-2)
        return Fn[i]


inputint = int(input())
print(moz(inputint))
