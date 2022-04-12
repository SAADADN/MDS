import os
import pickle
from MDSconstraint import MDSconstraint
import numpy as np

for filename in os.listdir("udgs/dataSolution"):
   with open(os.path.join("udgs/dataSolution", filename), 'rb') as f:
       network = pickle.load(f)
       #print(filename.split('_'))
   if (MDSconstraint(network['AdjacencyMatrix'].A, network['Solution'])):
       print('Feasible solution')
       print(np.sum(network['Solution']))
   else:
       print('Infeasible')