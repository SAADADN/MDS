import os
import pickle
import numpy as np

def MDSconstraint(A,x):
    for i in range(len(x)):
        if np.dot(x,A[i])<1:
            return False
    return True

for filename in os.listdir("udgs/dataSolution"):
   with open(os.path.join("udgs/dataSolution", filename), 'rb') as f:
       network = pickle.load(f)
       #print(filename.split('_'))
   if (MDSconstraint(network['AdjacencyMatrix'].A, network['Solution'])):
       print('Feasible solution')
       print(np.sum(network['Solution']))
   else:
       print('Infeasible')
