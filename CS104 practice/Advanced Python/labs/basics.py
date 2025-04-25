'''
    NumPy and The Matrix
'''

import numpy as np

def task1(matrix):
    '''return the upper diagonal matrix in column-wise fashion'''
    n=matrix.shape[0]
    ar=np.zeros((n,n), dtype=int)
    for i in range(n):
        for j in range(i,n):
            ar[i,j]=matrix[i,j]
    
    return ar.T

def task2(matrix):
    '''return mean, median, std (precision 2), all along x, determinant, inverse, pseudo-inverse'''
    mean = np.around(np.mean(matrix, axis=0), 2)
    median = np.around(np.median(matrix, axis=0), 2)
    std = np.around(np.std(matrix, axis=0), 2)
    det =  np.round(np.linalg.det(matrix), 2)
    inv = np.around(np.linalg.inv(matrix), 2)
    pseudoinv = np.around(np.linalg.pinv(matrix), 2)
    return mean, median, std, det, inv, pseudoinv

def task3(matrix, num = 0, padding = 3):
    '''return the padded matrix'''
    paddedmat=np.pad(matrix, padding, 'constant', constant_values=num)
    return paddedmat

if __name__ == '__main__':

    matrix = np.array([
        [5,5,84,3,9],
        [6,11,1,55,58],
        [1,20,48,12,36],
        [8,4,41,93,98],
        [6,17,64,0,13]
    ])

    # you can call the functions here
    # Uncomment the following lines to test your code

    # TASK 1
    print(task1(matrix))

    # TASK 2
    mean, median, std, det, inv, pseudoinv = task2(matrix)
    print("Mean: ", mean)
    print("Median: ", median)
    print("Standard Deviation: ", std)
    print("Determinant: ", det)
    print("Inverse: ", inv)
    print("Pseudo-Inverse: ", pseudoinv)

    # TASK 3
    print(task3(matrix, 10, 1)) # default padding