def exercice1():
    init_state = [3,4,3,1,2]
    print("Initial state : " + str(init_state))
    
    nbOfDays = 80
    currentDay = 1
    
    while currentDay <= nbOfDays:
        for i in range(len(init_state)):
            if(init_state[i] != 0):
                init_state[i] = init_state[i] - 1
            else:
                init_state[i] = 6
                init_state.append(8)
        print("After " + str(currentDay) + " day(s)" + str(init_state))
        currentDay+=1
    

    print("Number of lanternfish : " + str(len(init_state)))

if __name__=='__main__':
    exercice1()