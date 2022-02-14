import random

def exercice1():
    inputArray = [199,200,208,210,200,207,240,269,260,263,263]
    
    for i in range(len(inputArray)):
        if i != 0:
            if(inputArray[i-1] < inputArray[i]):
                print(str(inputArray[i]) + " increased")
            elif(inputArray[i-1] > inputArray[i]):
                print(str(inputArray[i]) + " decreased")
            else:
                print(str(inputArray[i]) + " unchanged")
        else:
            print(str(inputArray[i]) + " N/A - no previous measurement")
            
def exercice2():
    inputArray = random.sample(range(200, 400), 10)
    return_str = ""
    
    for i in range(len(inputArray)):
        
        if i != 0:
            if(inputArray[i-1] < inputArray[i]):
                return_str += str(inputArray[i]) + " increased"
            elif(inputArray[i-1] > inputArray[i]):
                return_str += str(inputArray[i]) + " decreased"
            else:
                return_str += str(inputArray[i]) + " unchanged"
        else:
            return_str += str(inputArray[i]) + " N/A - no previous measurement"
        return_str += "\n"
        
    return return_str


if __name__=='__main__':
    exercice1()
    print("------------------------------------")
    print(exercice2())