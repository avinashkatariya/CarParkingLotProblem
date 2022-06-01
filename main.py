from parkinglot import ParkingLot

def main():
  inputFile = open('input.txt','r')
  readLines = inputFile.readlines()
  inputFile.close()

  #creating parkingLot Instance
  parkingLot = ParkingLot()
  
  for command in readLines:
    try:
      command = command.replace("\n","")
      args = command.split(" ")
      func = parkingLot.getFunctionFromString(args[0])
      output = func(*args[1:])
      print(output)
    except:
      print("Invalid Command or Arguments")

if __name__ == '__main__':
  main()
