
def bSort(A):

    while True:
        swapped = False
        for i in range(1,len(A)):
            if A[i-1] > A[i]:
                swapped = True
                A[i-1], A[i] = A[i], A[i-1]

        if not swapped:
            return A

if __name__ == '__main__':

    A = [3,5,1,6,34,6,3,6,8,3]

    print('unsorted list:',A)

    Asorted = bSort(A)

    print('sorted list:',Asorted)
