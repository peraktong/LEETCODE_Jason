# build a tree recursively
# This is a simple k=1 KD tree. In future, we can split them based on rows:
# Eg: len(bin(num))-2

class Node():
    def __init__(self,data):
        self.data =data
        self.left = None
        self.right = None
        self.kd_array = []

    def Print(self):

        # print from small to big

        if self.left:
            self.left.Print()

        print(self.data)

        if self.right:
            self.right.Print()




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
        if self.data:
            if data<self.data:
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

    def find_kd(self,value,distance):
        none=1





x=[2,1,3,12,4,6,7]
root = Node(x[0])
for i in range(1,len(x)):
    root.insert(x[i])

root.Print()

# find:
print("Find value")
print(root.find_kd(value=7,distance=1.5))



