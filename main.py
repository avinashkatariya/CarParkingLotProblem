#This is python object to store parking entries
class ParkingEntry:
  def __init__(self,regNumber,driverAge,slot):
    self.regNumber = regNumber
    self.driverAge = driverAge
    self.slot = slot
    

class ParkingLot:
  #initalizing the class variables 
  def __init__(self):
    #creating array to store parking lot entries
    #because car can leave from any place.
    self.parkingLot = []
    self.parkingLotSize = 0
    #creating dict to return required result in O(n)
    self.ageHash = {}
    #creating dict to return required result in O(n)
    self.regNumberHash = {}

  #function to create parking lot and initialize the parking lot array
  def createParkingLot(self,size):
    self.parkingLotSize = int(size)
    for i in range(self.parkingLotSize):
      self.parkingLot.append(None)
    return f"Created parking of {self.parkingLotSize} slots"
    
  #function to return next empty parking lot
  def getFirstEmptySlot(self):
    for i in range(len(self.parkingLot)):
      if self.parkingLot[i] is None:
        return i
    #returning -1 if parking is full
    return -1

  #function to park car at next empty parking lot
  def parkCar(self,regNumber,gb,driverAge):
        
    firstEmptySlot = self.getFirstEmptySlot()
        
    if firstEmptySlot >= 0 :
      self.parkingLot[firstEmptySlot] = ParkingEntry(regNumber,driverAge,firstEmptySlot+1)
            
      #creating age Hash 
      if driverAge not in self.ageHash:
        self.ageHash[driverAge] = [firstEmptySlot+1]
      else:
        self.ageHash[driverAge].append(firstEmptySlot+1)
            
      #creating Registeration number Hash
      self.regNumberHash[regNumber] = firstEmptySlot + 1

      return f"Car with vehicle registration number \"{regNumber}\" has been parked at slot number {firstEmptySlot+1}"
            
            
    else:
      return "Parking Lot is Full. unable to park."
    
  def leaveParking(self,slotNumberStr):
    slotNumber = int(slotNumberStr)
    if slotNumber > self.parkingLotSize:
      return f"Slot number {slotNumber}  doesn't exists. please provide correct command"
            
    elif self.parkingLot[slotNumber - 1] is not None:
      driverAge = self.parkingLot[slotNumber - 1].driverAge
      regNumber = self.parkingLot[slotNumber - 1].regNumber
      self.parkingLot[slotNumber - 1] = None

      #removing object from hash
      self.ageHash[driverAge].remove(slotNumber)
            
      del self.regNumberHash[regNumber]

      return f"Slot number {slotNumber} vacated, the car with vehicle registration number \"{regNumber}\" left the space, the driver of the car was of age {driverAge}"
    
    else:
      return f"Slot number {slotNumber} is already Empty"

  def getSlotsfromAge(self,age):
    if age in self.ageHash:
      output = []
      for x in self.ageHash[age]:
        output.append(str(x))
      return ",".join(output)
    else:
      return ""
    
  def getRegistrationNumbersfromAge(self,age):
    if age in self.ageHash:
      registrationsNumber = []
      for slot in self.ageHash[age]:
        registrationsNumber.append(self.parkingLot[slot].regNumber)
        return ",".join(registrationsNumber)
    else:
      return ""
    
  def getSlotNumberWithRegNumber(self,regNumber): 
    if regNumber in self.regNumberHash:
      return self.regNumberHash[regNumber]
    else:
      return f"Car with vehicle registration number {regNumber} is not parked in parking lot"
        
  def getFunctionFromString(self,string):
    functionDict = {
        'Create_parking_lot':self.createParkingLot,
        'Park': self.parkCar,
        'Leave': self.leaveParking,
        'Slot_numbers_for_driver_of_age': self.getSlotsfromAge,
        'Slot_number_for_car_with_number':self.getSlotNumberWithRegNumber,
        'Vehicle_registration_number_for_driver_of_age': self.getRegistrationNumbersfromAge
    }
        
    return functionDict[string]

def main():
  inputFile = open('input.txt','r')
  readLines = inputFile.readlines()
  inputFile.close()

  #creating parkingLot Instance
  parkingLot = ParkingLot()
  
  outputFile = open('output.txt','w')
  
  for command in readLines:
    command = command.replace("\n","")
    args = command.split(" ")
    func = parkingLot.getFunctionFromString(args[0])
    output = func(*args[1:])
    outputFile.write(str(output)+"\n")
  
  outputFile.close()

if __name__ == '__main__':
  main()
