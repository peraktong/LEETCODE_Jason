# build a tree recursively
class Node():
    def __init__(self,data):
        self.data =data
        self.left = None
        self.right = None

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






root = Node(12)
# root.Print()

# insert
root.insert(6)
root.insert(14)
root.insert(3)
root.Print()

# find:
print("Find value")
print(root.find_value(7))
print(root.find_value(14))


