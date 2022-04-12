import numpy as np

def MDSconstraint(A,x):
    for i in range(len(x)):
        if np.dot(x,A[i])<1:
            return False
    return True
