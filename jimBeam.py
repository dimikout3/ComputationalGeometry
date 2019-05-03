
def  areaTriangle(x1,y1,x2,y2):
    return abs(x1*y2 - x2*y1)/2

if __name__ == '__main__':

    x1, y1 = 2,2
    x2, y2 = 3,3

    xm, ym = 1,1

    OAOM = areaTriangle(x1,y1,xm,ym)
    OMOB = areaTriangle(xm,ym,x2,y2)

    OAOB = areaTriangle(x1,y1,x2,y2)
    MAMB = areaTriangle(x1-xm,y1-ym,x2-xm,y2-ym)

    # coolinear
    if (OAOM + OMOB) == (OAOB + MAMB):
        print('NO')
    else:
        print('YES')
