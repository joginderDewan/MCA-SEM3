def getName():
    return "Last name, first name"
    
class MyBST:
    def __init__(self, data):
        
        self.data = data
        self.left = None
        self.right = None

   
    
        
    
    def getLeft(self):
        return self.left
    
    def getRight(self):
        return self.right
    
    def getData(self):
        return self.data

    def insert(self, data):
       
        if self is None:
            return MyBST(data)
        # if self.data == data:
        #     return self
            
 
      
        if self.data < data:
            if self.right is None:
                self.right = MyBST(data)
            else:
                self.right = (self.right).insert(data)
        if self.data > data:
            if self.left is None:
                    self.left = MyBST(data)
            self.left = (self.left).insert(data)
        return self
    
    def getHeight(self):
        if self is None:
            return -1
        lh = -1
        if self.left is None:
            lh = -1
        else:
            lh = (self.left).getHeight()
        rh = -1
        if self.right is None:
            rh = -1
        else:
            rh = (self.right).getHeight()
        return 1 + max(lh,rh)

    def __contains__(self, data):
        
        if self is None:
            return False

        if self.data == data:
            return True
            
 
        if data > self.data:
            if self.right is not None:
                return (self.right).__contains__(data)
            else:
                return False
        else:
            if  self.left is not None:
                return (self.left).__contains__(data)
            else:
                return False
       

class MyAVL(MyBST):
    def __init__(self, data):
        
        super().__init__(data)
        self.ht = 0
        self.bal = 0

    def getBalanceFactor(self):
        
        lh = -1
        if self.left is None:
            lh = -1
        else:
            lh = self.left.ht
        rh = -1
        if self.right is None:
            rh = -1
        else:
            rh = self.right.ht

        return lh - rh

    def updateHeightAndBalance(self):
        lh = -1
        if self.left is None:
            lh = -1
        else:
            lh = self.left.ht
        rh = -1
        if self.right is None:
            rh = -1
        else:
            rh = self.right.ht

        self.bal =  lh - rh
        self.ht = max(lh,rh)+1

        

    def insert(self, data):
        
        
        if self is None:
            return MyAVL(data)
        
       
        if data >= self.data:
            if self.right is None:
                self.right = MyAVL(data)
            else:
                self.right = (self.right).insert(data)
                
        if data < self.data :
            if self.left is None:
                    self.left = MyAVL(data)
            else:
                self.left = (self.left).insert(data)

        return self.getRotation()

    def getRotation(self):
       

        self.updateHeightAndBalance()
        if(self.bal == 2):
            if self.left.bal == 1:
                rv = self
                rv = self.rightRotate()
                return rv
            else:
                lc = (self.left).leftRotate()
                self.left = lc
                rv = self
                rv = self.rightRotate()
                return rv
        if(self.bal == -2):
            if self.right.bal == -1:
                rv = self
                rv = self.leftRotate()
                return rv
            else:
                rc = (self.right).rightRotate()
                self.right = rc
                rv = self
                rv = self.leftRotate()
                return rv
        return self
  


    def leftRotate(self):
        
        A = self
      
        B = A.right
      
        Bleft = B.left
      

        B.left = A
        A.right = Bleft
       
        self.updateHeightAndBalance()
        B.updateHeightAndBalance()
        


        return B
        

    def rightRotate(self):
        
        A = self
        B = A.left
        Bright = B.right

        B.right = A 
        A.left = Bright

        self.updateHeightAndBalance()
        B.updateHeightAndBalance()

        return B

    def print(self):
        if self is None:
            return
        print(self.data)
        if self.left is not None:
            self.left.print()
        if self.right is not None:
            self.right.print()

    def print(self):
        if self is None:
            return
        lf = ''
        rf = ''
        if self.left is not None:
            lf = self.left.data
        if self.right is not None:
             rf = self.right.data
        print(lf,"<-" ,self.data,"->",rf)
        if self.left is not None:
            self.left.print()
        if self.right is not None:
            self.right.print()
        






        





