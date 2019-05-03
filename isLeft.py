
def isLeft(P0, P1, P2):
    """determines if P2 is on the left side of the P0P1 lane"""
    d = (P1[0]-P0[0])*(P2[1]-P0[1])  - (P2[0]-P0[0])*(P1[1]-P0[1])

    return (True if d>0 else False)


if __name__ == '__main__':

    P0 = [0, 0]
    P1 = [1, 1]
    P2 = [1, 5]

    b = isLeft(P0, P1, P2)

    print(b)
