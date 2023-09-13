class ParentClass:        # define parent class
   parentAttr = 100
   def __init__(self):
      print("Calling parent constructor")

   def parentMethod(self):
      print('Calling parent method')

   def setAttr(self, attr):
      ParentClass.parentAttr = attr

   def getAttr(self):
      print("Parent attribute :", ParentClass.parentAttr)

class ChildClass(ParentClass): # define child class
    def __init__(self):
        print("Calling child constructor")
    
    def childMethod(self):
        print('Calling child method')

    def callParentMethod(self):
        super().parentMethod()
    def callantmethod(self):
        self.parentMethod()

c = ChildClass()          # instance of child
c.childMethod()           # child calls its method
c.callParentMethod()      # calls parent's method
c.callantmethod()        # calls parent's method
