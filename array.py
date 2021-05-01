def num(a):

    res = a[0]
    for i in a:
        if res > i:
            res = i
    return res

array = (40, 7, 22, 78, 90, 12, 15, 20)

print(num(array))
