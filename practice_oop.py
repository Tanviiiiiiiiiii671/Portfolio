#class Subject:
    # name ="ketan"
   #  def __init__(self,fullname):
  #       self.name = fullname
 #        print("I am the best")
#s1=Subject("karan")
#print(s1.name)
       # s1 = Subject()
 
       #print(s1.name)



#class Subject:
    #__name = "hello"
   
    #def __hello(self):
   #     print("hey there it's me !!!!!")
  #  def welcome(self):
 #       self.__hello
#p1 = Subject()  
#print(p1.welcome())
    
    #def __init__(self):
        #self.name=name
        #self.rollno = rollno    
#class Car:
    #@staticmethod
    #def start():
    #    print("car is started")
   # @staticmethod
  #  def stop():
 #       print("car is stoped...")  
#class Toyotacar(Car): 
  #   def __init__(self,name):
 #       self.name = name
#car1 = Toyotacar("Fortuner")
#car2 = Toyotacar("innova")
#car1.start()
class Car:
    def start(self):
        self.__engine()  # hidden private method
        print("Car started")

    def __engine(self):  # hidden detailed working
        print("Engine ignition process started...")
car = Car()    # create object
car.start()    # call method using object

#Car.start()

