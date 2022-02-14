import random

def generate_grid():
    tab = list()
    ligne = list()
    for r in range(5):
        for c in range(5):
            ligne.append(random.randint(0,25))
        tab.append(ligne)
        ligne = list()
    return tab

def exercice1():
    
    tab1 = generate_grid()
    print(tab1)
    
    
    
    winner = False
    while winner == False:
        new_number = random.randint(0,25)
        print(new_number)
        for r in range(5):
            for c in range(5):
                if(new_number == tab1[r][c]):
                    tab1[r][c] = "M"
        
        winner = True
        
        for r in range(5):
            if tab1[r][0] != "M":
                winner = False
    print(tab1)
        
        

def old():
    for r in range(5):
        for c in range(5):
            print(random.randint(0,25),end = " ")
        print()

if __name__=='__main__':
    exercice1()