import random
import winsound

class TrainCar:
  def __init__(self, type, duration = None, frequency = None, next=None): 
    self.type = type
    self.ID = random.randrange(100, 1000)
    self.isFull = True
    self.duration = duration
    self.frequency = frequency
    self.next = next
#---------------------------------------------
class FreightTrain:
  def __init__(self):  
    self.head = None 
  
  def insert(self, type, duration=None, frequency=None):
      newCar = TrainCar(type, duration, frequency) #instantiate a new student node
      if self.head: #check if a head exists
          current = self.head #create a temporary pointer to the head node
          #while there's another node in the line, "walk" down the line until the end
          while current.next:  
              current = current.next
          current.next = newCar #add the new student to the end
      else:
          self.head = newCar #if there was no head student, insert at front of empty line
          
  def printList(self):
      current = self.head
      while current:
          print("Train car #",current.ID, "is of type:", current.type, "and", end = " ")
          if current.isFull == True:
              print("is full")
          else:
              print("is empty")
          current = current.next
          
  def IDsearch(self, num):
      current = self.head
      while current:
          if current.ID == num:
              print("Found it! Train car #", current.ID, "is a(n)", current.type, "car and", end=" ")
              if current.isFull == True:
                  print("is full.")
              else:
                  print("is empty.")
              return 0
          current = current.next
      print("Sorry, could not find a train car with the number", num)

  def CargoSearch(self, type):
      counter = 0
      current = self.head
      while current:
          if current.type == type:
              print("Train car #", current.ID, "is a(n)", current.type, "car.")
              counter+=1
          current = current.next
      print("There are", counter, type, "cars on this train.")
      
  def TOOT(self):
      current = self.head
      while current:
          if current.type == "engine":
              winsound.Beep(current.frequency, current.duration)
              winsound.Beep(current.frequency, current.duration)#trens always toot twice!
          current = current.next

#---------------------------------------------
Train1 = FreightTrain()
doExit = False
#HOWDY DOODY ITS THE GAME LOOP YALL#############################################
while doExit == False:
    print()
    print("-----------------------------------------------------------------")
    print("Press 1 to add item to train, 2 to print entire train,")
    print("3 to search by train car ID, 4 to search by cargo, 5 to BEEP HORNS")
    print("5 to BEEP HORNS, or 6 to quit:")
    choice = int(input())
    
    #ADDING TRAIN CARS
    if choice == 1:
        CarType = input("Enter type (engine, coal, oil, auto, shipping):")
        if CarType == "engine":
            freq = int(input("Enter horn frequency:"))
            dur = int(input("Enter horn duration:"))
            Train1.insert(CarType, dur, freq)
        else:
            Train1.insert(CarType)
            
    #PRINTING TRAIN CARS       
    elif choice == 2:
        print("Printing train:")
        Train1.printList()
        
    #SEARCH BY ID
    elif choice == 3:
        ID = int(input("Enter the ID of the traincar you are looking for:"))
        Train1.IDsearch(ID)
    
    #SEARCH BY CARGO
    elif choice == 4:
        cargo = input("Enter the cargo type you are looking for:")
        Train1.CargoSearch(cargo)
    #TOOTS
    elif choice == 5:
        print("TOOT TOOT!")
        Train1.TOOT()
        
    #QUIT
    elif choice == 6:
        print("thank you for using the train management program.")
        doExit = True
        
    else:
        print("Sorry, not a valid response")
        
print("goodbye")
