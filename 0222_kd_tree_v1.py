import numpy as np
import collections
from copy import deepcopy


class KD_node():
    def __init__(self,value):
        self.value = value

        self.left = None
        self.right =None

        #
        self.data_lower = None
        self.data_upper = None



class KD_tree():
    __slot__=("data","data_left")
    def __init__(self,data):
        self.data = data
        self.N = data.shape[0]
        self.k = data.shape[1]
        print(self.N,self.k)
    # find the minimum distance+index in dth dimension for point x in data
    def _find_min_d(self,point,d):

        if d>self.k:
            print("Error: Exceed dimension of the input data")

        index = np.argmin(point[d]-self.data[:,d])

        return index,abs(point[d]-self.data[index,d])


    def construct_KD_tree(self):
        root = KD_node(self.data[0,:])
        self.data_left = self.data_left[1:,:]

        for i in range(0,len(self.N)):
            if root.data:
                none=1





# input is N*k, where k is the dimension

data_array = np.random.rand(100,3)*250-125


model = KD_tree(data = data_array)



