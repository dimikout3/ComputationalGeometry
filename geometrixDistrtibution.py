# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def run(n, p):

    q = 1 - p
    rtn = math.pow(q,n-1)*p
    return rtn

if __name__ == "__main__":
    n = 5
    p = 1/3

    rtn = 0.
    for i in range(1,n+1):
        rtn = rtn + run(i, p)
        print(i)
        print(rtn)
    # rtn = run(n,p)
    print(round(rtn,3))
