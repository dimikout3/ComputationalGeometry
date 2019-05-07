# Enter your code here. Read input from STDIN. Print output to STDOUT
from cmath import phase
import math

def solve(A):

    angles = []
    for x,y in A:
        # angles.append([math.degrees(phase(complex(x,y))),x,y])
        angles.append([phase(abs(complex(x,y))),x,y])

    print('pre-sorted angles ',angles)
    angles.sort()
    print('angles ',angles)
    rtn = [[x,y] for a,x,y in angles]
    return rtn

if __name__ == "__main__":

    A = [[1,0],[0,-1],[-1,0],[0,1]]
    # A = [[-25,-99],[37,-100],[-80,4],[-83,11],[12,-28]]

    solution = solve(A)
    # rtn = run(n,p)
    print(solution)
