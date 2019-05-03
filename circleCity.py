import math

def solve(d, k):

    radius = math.sqrt(d)
    rInt = int(radius)
    sets = []
    s = 0
    y=0

    for x in range(rInt, 0, -1):
        dxy = x**2 + y**2

        while dxy < d:
            y += 1
            dxy = x**2 + y**2

        if dxy == d:
            s += 1
            sets.append([x,y])

        print(x,y)

    s *= 4

    # print(radius)
    print(sets)
    if s <= k:
        return 'possible'
    else:
        return 'impossible'

d = 25
k = 12
print( solve(d,k) )
