def ucln(num1, num2):
    while num1 != num2:
        if num1 > num2:
            num1 -= num2
        else:
            num2 -= num1
    return num1

def phan_so(num1, num2):
    u = ucln(num1, num2)
    return ("%d/%s" % (num1/u, num2/u))