import numpy as np
n=int(input('Enter the oder for n x n  matrix: '))


print(f'Enter the {n} x {n} elements : ')
ele = list(map(int , input().split()))

matrix = np.array(ele).reshape(n,n)
print(matrix)

c=0
for i in range(n):
    c+=matrix[i][i]
print(f'The sum of diagonal elements in {n}x{n} matrix is {c}')    
    
    
