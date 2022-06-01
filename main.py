from parkinglot import ParkingLot

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
