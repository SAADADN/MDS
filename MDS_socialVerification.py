import numpy as np
import os
import pickle

def MDSconstraint(A,x):
    for i in range(len(x)):
        if np.dot(x,A[i])<1:
            return False
    return True

for filename in os.listdir("MDS_social"):
   print(filename)
   with open(os.path.join("MDS_social", filename), 'rb') as f:
       network = pickle.load(f)
   if MDSconstraint(network['AdjacencyMatrix'].A,network['Solution']):
       print('Feasible')
       print(np.sum(network['Solution']))
   else:
        print('Infeasible')
