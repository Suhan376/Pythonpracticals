import sympy as sy
M=sy.Matrix([[1,2,3],[2,3,4],[4,8,9]])
print("the row echelon form of matrix m")
print(M.rref())
print("the rank of the matrix m=",M.rank())