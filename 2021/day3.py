def exercice1():
    input = ["00100","11110","10110","10111","10101","01111","00111","11100","10000","11001","00010","01010"]
    
    gamma_rate = ""
    epsilon_rate = ""
    
    
    for i in range(len(input[0])):
        nb_0 = 0
        nb_1 = 0  
        for j in range(len(input)):
            if input[j][i] == "0":
                nb_0 += 1
            else:
                nb_1 += 1
        
        if(len(input)-nb_0 > len(input)-nb_1):
            gamma_rate += "1"
            epsilon_rate +="0"
        else:
            gamma_rate += "0"
            epsilon_rate +="1"
            
    print(gamma_rate)
    print(epsilon_rate)
    
    return int(gamma_rate,2)*int(epsilon_rate,2)
    
if __name__=='__main__':
    print(exercice1())