def exercice1():
    keep = True
    horizontal_pos = 0
    depth = 0
    
    while(keep):
    
        MooveInput = int(input("Type a number to select the mouvement : \n 1. forward  \n 2. down  \n 3. up \n\n"))
        UnitInput = int(input("By how much : "))
        
        if(MooveInput == 1):
            horizontal_pos += UnitInput
        elif(MooveInput == 2):
            depth += UnitInput
        elif(MooveInput == 3):
            depth -= UnitInput
        
        keep_going = input("Keep going y/n: ")
        if(keep_going == "n"):
            keep = False
        
    return horizontal_pos*depth
        
if __name__=='__main__':
    print(exercice1())