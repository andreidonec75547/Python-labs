l = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]


for x in l:
    n = 1
    sumon = []
    i = 0
    while abs(n) >= 0.0001:

        num = (2*i)

        factorial = 1

        while num > 1:
            factorial = factorial * num
            num = num - 1

        n = ((-1)**i)*((x**(2*i))/factorial)
        sumon.append(n)

        i += 1

    print(sum(sumon), sumon)


# import math
#
# for x in l:
