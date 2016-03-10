import numpy as np
import scipy
import scipy.linalg as linalg

def lu(A, b):
    sol = []
    # Edit here to implement your code    
    L , U = linalg.lu(A, True)
    y = linalg.solve(L,b)
    x = linalg.solve(U, y)
    sol.append(x)
    return list(sol)

def sor(A, b):
    sol = []
    # Edit here to implement your code
    maxiter = 15
    n = len(A)
    #A = D - L - U
    D = np.zeros((n,n))
    L = np.zeros((n,n))
    U = np.zeros((n,n))
    for i in range(0, n):
        D[i][i] = A[i][i]
    for i in range(0, n):
        for j in range(0, i):
            L[i][j] = -A[i][j]
    for i in range(0, n):
        for j in range(i+1, n):
            U[i][j] = -A[i][j]
    
    #K = inv(D)(L+U)
    K = np.zeros((n,n))
    for i in range(0, n):
        K[i][i] = 1/D[i][i]
    K = np.dot(K,(L+U))
    lamda = max(abs(linalg.eigvals(K)))
    lamda = np.square(lamda)
    omega = 2 * (1 - np.sqrt(1-lamda)) / lamda
    
    Q = np.zeros((n,n))
    Q = 1/omega * (D - omega * L)
    x = np.zeros(n)
    for iteration in range(0, maxiter):
        x = np.dot(np.dot(np.linalg.inv(Q), (Q-A)) , x) + np.dot(np.linalg.inv(Q) , b)
        sol.append(x)
        
    return list(sol)

def check(A):
    try:
        temp = 2 * np.diag(A) > np.sum(np.abs(A),1)
        result = temp.all()
        
        if (result):
            #A is Strictly Diagonally dominant Matrix
            return True
            
        #Check positive Definite Matrix
        np.linalg.cholesky(A)
        
        #positive diaganal element
        temp = np.diag(A) > 0
        result = temp.all()
        if (~result):
            #some diagonal element is negative
            return True
    except np.linalg.linalg.LinAlgError:
        #Solve by LU
        return True
    return False

def solve(A, b):
    condition = check(A) # State and implement your condition here
    if condition:
        print('Solve by lu(A,b)')
        return lu(A,b)
    else:
        print('Solve by sor(A,b)')
        return sor(A,b)

if __name__ == "__main__":
    ## import checker
    ## checker.test(lu, sor, solve)

    A = [[2,1,6], [8,3,2], [1,5,1]]
    b = [9, 13, 7]
    sol = solve(A,b)
    print(sol)
    
    A = [[6566, -5202, -4040, -5224, 1420, 6229],
         [4104, 7449, -2518, -4588,-8841, 4040],
         [5266,-4008,6803, -4702, 1240, 5060],
         [-9306, 7213,5723, 7961, -1981,-8834],
         [-3782, 3840, 2464, -8389, 9781,-3334],
         [-6903, 5610, 4306, 5548, -1380, 3539.]]
    b = [ 17603,  -63286,   56563,  -26523.5, 103396.5, -27906]
    sol = solve(A,b)
    print(sol)
