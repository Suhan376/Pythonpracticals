import numpy as np
def matrix(R,C):
    A = np.zeros([R,C])
    print("Enter the matroc row  wise")
    for i in range(R):
        for j in range(C):
            A[i][j]=int(input())
    print("the print matrix A",A)
    return A
R=int(input("enter no. of rows"))
C=int(input("enter no. of columns "))
A=matrix(R,C)
print("nextmatrixB")
B=matrix(R,C)
print("print the addition of two matrices",A+B)
print("print the subtractions of two matrices",A-B)
