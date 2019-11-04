# build a tree recursively
# Here the binary tree is not sorted in order.
class Node():
    def __init__(self,data):
        self.data =data
        self.left = None
        self.right = None


    def find_value(self,value):
        if value < self.data:
            if self.left ==None:
                print("Not Found")
                return None
            return self.left.find_value(value)
        elif value > self.data:
            if self.right ==None:
                print("Not Found")
                return None
            return self.right.find_value(value)
        else:
            print("%.2f is found"%self.data)




    def insert(self,data):
        # If we already have the root
        if data:
            if self.data:
                if data < self.data:
                    if self.left == None:
                        # recursively
                        self.left = Node(data)
                    else:
                        self.left.insert(data)
                # We put equal element to the right:
                else:
                    if self.right is None:
                        # recursively
                        self.right = Node(data)
                    else:
                        self.right.insert(data)
            else:
                self.data = data
        else:
            data=-1
            if self.data:
                if data < self.data:
                    if self.left == None:
                        # recursively
                        self.left = Node(None)
                    else:
                        self.left.insert(None)
                # We put equal element to the right:
                else:
                    if self.right is None:
                        # recursively
                        self.right = Node(None)
                    else:
                        self.right.insert(None)
            else:
                self.data = None







x=[2,1,3,None,4,None,7]
root = Node(x[0])
for i in range(1,len(x)):
    root.insert(x[i])

# find:
print("Find value")
print(root.find_value(7))
print(root.find_value(14))


