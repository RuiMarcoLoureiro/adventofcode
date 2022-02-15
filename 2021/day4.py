import random

def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True

def generate_grid():
    tab = list()
    ligne = list()
    for r in range(5):
        for c in range(5):
            ligne.append(random.randint(0,25))
        tab.append(ligne)
        ligne = list()
    return tab

def checkCol(col):
    if col and all(elem == "M" for elem in col):
        return True
    else:
        return False

def countAttempts(tab1):
    
    #tab1 = generate_grid()
    #print(tab1)
    
    count = 0
    winner = False
    while winner == False:
        count += 1
        new_number = random.randint(0,25)
        #print("rnd nb " + str(new_number))
        for r in range(5):
            for c in range(5):
                if(new_number == tab1[r][c]):
                    tab1[r][c] = "M"

        col1,col2,col3,col4,col5 = zip(*tab1)

        columns = [col1,col2,col3,col4,col5]
        
        for i in range(5):
            if checkCol(columns[i]):
                print("COL" + str(i+1))
                winner = True
            elif checkCol(tab1[i]):
                print("LINE" + str(i+1))
                winner = True
             
    print(tab1)
    print(count)
    
    return count
        
def exercice1():
    print("----------------------------")
    tab1 = generate_grid()
    print(tab1)
    count1 = countAttempts(tab1)
    print("----------------------------")
    tab2 = generate_grid()
    print(tab2)
    count2 = countAttempts(tab2)
    print("----------------------------")
    tab3 = generate_grid()
    print(tab3)
    count3 = countAttempts(tab3)
    
    counts = [count1,count2,count3]
    
    if count1 == min(counts):
        print("Grille 1 GAGNE")
    elif count2 == min(counts):
        print("Grille 2 GAGNE")
    else:
        print("Grille 3 GAGNE")

if __name__=='__main__':
    exercice1()