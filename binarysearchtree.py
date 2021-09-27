class foodMenu:

    
    def __init__(self, foodName, foodPrice):
        self.foodDetails = [foodName, foodPrice]
        self.leftChildNode = None
        self.rightChildNode = None
        

        
    def addNode(self, name, price):
        if name == self.foodDetails[0]:
            return # node already exist

        
        if name < self.foodDetails[0]:
            if self.leftChildNode:
                self.leftChildNode.addNode(name, price)
            else:
                self.leftChildNode = foodMenu(name, price)

            
        else:
            if self.rightChildNode:
                self.rightChildNode.addNode(name, price)
            else:
                self.rightChildNode = foodMenu(name, price)


    def findNode(self, name):
        

        
        if self.foodDetails[0] == name:
            return True
        


        if name < self.foodDetails[0]:
            if self.leftChildNode:
                return self.leftChildNode.findNode(name)
            else:
                return False
        


        if name > self.foodDetails[0]:
            if self.rightChildNode:
                return self.rightChildNode.findNode(name)
            else:
                return False
            
 

    def inOrderTraversal(self):
        elements = []
        if self.leftChildNode:
            elements += self.leftChildNode.inOrderTraversal()

        elements.append(self.foodDetails)

        if self.rightChildNode:
            elements += self.rightChildNode.inOrderTraversal()

        return elements
