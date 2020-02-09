from decimal import Decimal as D, getcontext

def gauss_legendre(precision):
    getcontext().prec = precision + 2
    a = [1]
    b = [1 / D(2).sqrt()]
    t = [D(.25)]
    p = [1]
    c = 1
    while c <= (precision // 2) + 1:
        a.append((a[c - 1] + b[c - 1]) / D(2))
        b.append(D(a[c - 1] * b[c - 1]).sqrt())
        t.append(t[c - 1] - p[c - 1] * ((a[c - 1] - a[c]) ** 2))
        p.append(2 * p[c - 1])
        c += 1
    pi_calc = ((a[-1] + b[-1]) ** D(2)) / (4 * t[-1])
    return D(str(pi_calc)[0:-1])

if __name__ == "__main__":
    num = input("Please enter the precision you want:")
    my_pi = str(gauss_legendre(int(num)))
    print("Pi is approximately", my_pi)



