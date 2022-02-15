def readInput():
    tmp = []
    f = open('inputDay1.txt')
    for line in f.readlines():
        tmp.append(int(line))
    f.close()
    
    return tmp

def ex1():
    inputArray = readInput()
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
    print(ex1())