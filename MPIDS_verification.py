import numpy as np
import os
import pickle

def MPIDSconstraint(A,x):
    for i in range(len(x)):
        if np.dot(x,A[i])<np.sum(A[i,:])/2:
            return False
    return True

for filename in os.listdir("MPIDS_Table9"): #change the directory name to MPIDS to verify the results in Table 8
   print(filename)
   with open(os.path.join("MPIDS_Table9", filename), 'rb') as f:
       network = pickle.load(f)
   constr=lambda x:MPIDSconstraint(network['AdjacencyMatrix'].A, x)
   if constr(network['Solution']):
       print('Feasible')
       print(np.sum(network['Solution']))
   else:
        print('Infeasible')




