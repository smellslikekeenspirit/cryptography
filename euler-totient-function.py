
def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def phi(n):
    print("Gcd of 1" + " and " + str(n) + " is 1")
    result = 1
    for i in range(2, n):
        x = gcd(i, n)
        if x == 1:
            print("Gcd of " + str(i) + " and " + str(n) + " is " + str(x))
            result += 1
        else:
            print("Gcd of " + str(i) + " and " + str(n) + " is " + str(x))
    return result


for n in range(940, 943):
    print("phi(", n, ") = ",
          phi(n), sep="")

