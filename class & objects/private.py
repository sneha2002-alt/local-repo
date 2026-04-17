class Person:
    __name = "anonymous" # private attribute
    
    def __hello(self):
        print("hello person") # private method
        
    def welcome(self):
        self.__hello()   
        
p1 = Person()

# print(p1.__name)
# p1.__hello()
p1.welcome()        