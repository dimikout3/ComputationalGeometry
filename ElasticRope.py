import matplotlib.pyplot as plt
# import numpy as np

# https://en.wikipedia.org/wiki/Convex_hull
# https://en.wikipedia.org/wiki/Convex_hull_algorithms

def findReferencePoint(A):

    # Anp = np.array(A)
    # Anp = Anp.T
    #
    # # first instance of minimun y-coordinate
    # yIndex = np.argmin(Anp, axis = 1)[1]
    # y = Anp[1][yIndex]
    # x = Anp[0][yIndex]
    #
    # yNext = Anp[1][yIndex+1]
    # xNext = Anp[0][yIndex+1]
    # while yNext <= y and yIndex < len(Anp):
    #
    #     if xNext > x:
    #         yIndex += 1
    #
    #         x = Anp[0][yIndex]
    #         y = Anp[1][yIndex]
    #
    #         yNext = Anp[1][yIndex+1]
    #         xNext = Anp[0][yIndex+1]

    yMin = 10000000
    xPair = -10000000
    for x,y in A:

        if y < yMin:
            yMin = y
            xPair = x
        elif y == yMin:
            if  x > xPair:
                xPair = x


    return [xPair, yMin]

def isLeft(P0, P1, P2):
    """determines if P2 is on the left side of the P0P1 lane"""
    d = (P1[0]-P0[0])*(P2[1]-P0[1])  - (P2[0]-P0[0])*(P1[1]-P0[1])

    return (True if d>0 else False)

def bSort(P0, A):

    while True:
        swapped = False
        for i in range(1,len(A)):
            # if A[i-1] > A[i]:
            if not isLeft(P0, A[i-1], A[i]):
                swapped = True
                A[i-1], A[i] = A[i], A[i-1]

        if not swapped:
            return A

def printOrder(x, y, A):

    for xR,yR in A:
        plt.scatter(x,y, color ='blue')
        plt.scatter(xR,yR, color ='red')
        plt.show()
        plt.close()

def convexStack(P0, A):

    S = []
    S.append( P0 )
    S.append( A.pop(0) )

    i=0
    while i<len(A):
        print(S)
        P1 = S[-1]
        P2 = S[-2]

        if not isLeft(P1, P2, A[i]):
            S.append(A[i])
            i += 1
        else:
            S.pop(-1)

    return S

def findConvexHull(A):

    P0 = findReferencePoint(A)
    A.remove(P0)

    A = bSort(P0, A)

    S = convexStack(P0, A)

    return S


if __name__ == '__main__':

    a = 4
    b = 1

    a,b = (a,b) if a<b else (b,a)

    # A = [[100, 100],[200, 100],[200, 200],[100, 200]]
    A = [[167, 84],[421, 84],[283, 192],[433, 298],[164, 275],[320, 133]]
    print('A is =',A)

    A1 = A[a-1:b]
    A2 = A[-1:b-2:-1] + A[a-1:0:-1] + [A[0]]

    x = [i[0] for i in A]
    y = [i[1] for i in A]

    # x += [A[0][0]]
    # y += [A[0][1]]
    #
    # plt.plot(x, y)
    # plt.show()
    # Write Your Code Here

    S1 = findConvexHull(A1)
    S2 = findConvexHull(A2)

    # P0 = findReferencePoint(A)
    # A.remove(P0)
    #
    # print('P0 is =',P0)
    #
    # A = bSort(P0, A)
    # print('Radial sorted A =',A)
    #
    # # printOrder(x, y, A)
    # S = convexStack(P0, A)
    # print('Convex hull is determined by points:',S)
    print('Convex hull is determined by points:',S1)
    print('Convex hull is determined by points:',S2)
