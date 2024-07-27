## Question 1

grille = [[7, 8, 1, 4, 5, 2, 6, 9, 3],
        [5, 6, 3, 9, 1, 7, 2, 4, 8],
        [2, 4, 9, 6, 3, 8, 5, 1, 7],
        [3, 5, 4, 2, 8, 6, 1, 7, 9],
        [6, 7, 2, 1, 9, 4, 3, 8, 5],
        [9, 1, 8, 5, 7, 3, 4, 2, 6],
        [4, 9, 5, 8, 6, 1, 7, 3, 2],
        [1, 3, 6, 7, 2, 9, 8, 5, 4],
        [8, 2, 7, 3, 4, 5, 9, 6, 1]]

grille = [[7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]]

def affiche_grille(grille):
    """affiche la grille

    Args:
        grille ([[int]]): la grille à afficher
    """
    print("==========================")
    for index, ligne in enumerate(grille): #enumerate pour avoir l'indexage et la valeur
        print("|", end = ' ')
        for num, case in enumerate(ligne): 
            print(case, end = ' ')
            if num%3-2 == 0: print("|", end = ' ') #toutes les 3 cases on ajoute une barre
        print()
        if index%3-2 == 0: print("==========================") #toutes les 3 lignes on ajoute une barre

affiche_grille(grille)

## Question 2
def addList(listes):
    """permet de joindre des listes

    Args:
        listes ([[int]]): liste de liste

    Returns:
        [int]: une liste unique
    """
    sum = list()
    for liste in listes:
        sum += liste
    return sum

def getBoxes(grille, listOfListForm=False):
    """renvoi une liste des boites

    Args:
        grille ([[int]]): la grille
    Return:
        [[int]] : la liste des boites
    """
    boites = list()
    for index, ligne in enumerate(grille):
        if index%3 == 0: 
            for i in range(3): boites.append(list())
        boites[-3].append(ligne[:3]) #recupère les 3 premières cases de la ligne, et les stocks dans l'avant-avant dernière boite
        boites[-2].append(ligne[3:6])
        boites[-1].append(ligne[6:9])

    if listOfListForm: return boites
    return([addList(boite) for boite in boites])

def est_complete(grille):
    """verifie si la grille est complete et correcte

    Args:
        grille ([[int]]): la grille à vérifier
    Return:
        Boolean : True si oui, False sinon
    """
    #on vérifie que les lignes sont correctes
    for ligne in grille:
        for num in range(1, 10): 
            if num not in ligne: return False

    #on vérifie que les colonnes sont correctes
    for ligne in range(len(grille)):
        colonne_actuelle = list()
        for colonne in range(len(grille[ligne])):
            colonne_actuelle.append(grille[colonne][ligne])
        for num in range(1, 10):
            if num not in colonne_actuelle: return False

    #on vérifie que les boites sont correctes
    for boite in getBoxes(grille):
        for num in range(1, 10):
            if num not in boite: return False
    return True

print(est_complete(grille))

## Question 3
def chiffre_possible(grille, i, j):
    """trouve les chiffres possibles d'une case

    Args:
        grille ([[int]]): la grille
        i (int): numéro de ligne
        j (int): numéro de colone

    Returns:
        [int]: liste des valeurs possibles
    """
    boites = getBoxes(grille)
    num_boite = int(i/3)*3+int(j/3) #on récupère le numéro de la boite
    boite = boites[num_boite]
    possibles = list()

    for num in range(1, 10):
        if num not in boite and num not in grille[i] and num not in [l[j] for l in grille]: possibles.append(num) #on ajoute la valeur dans les possible si elle respecte les règles du sudoku
    
    return possibles

chiffre_possible(grille, 8, 0)

## Question 4
def solveur_naif(grille):
    """resoud la grille avec la première méthode

    Args:
        grille ([[int]]): la grille
    """
    while not est_complete(grille): #tant que la grille n'est pas complète
        for i in range(len(grille)):
            for j in range(len(grille[i])):
                if grille[i][j] == 0: #on parcours les cases, et on vérifie que la case est vide
                    solutions = chiffre_possible(grille, i, j) 
                    if len(solutions) == 1: grille[i][j] = solutions[0] #si le nombre de chiffre possible = 1, on le note dans la grille
        print("############################")
        affiche_grille(grille)
    
solveur_naif(grille)

## Question 5
def getIJFromBox(numBox, i, j):
    """Permet de recuperer les vraies coordonnées d'une case depuis une boite

    Args:
        numBox (int): Numero de la boite
        i (int): i dans la boite
        j (int): j dans la boite
    """
    real_i, real_j = None, None
    real_i = i+3*int(numBox/3)
    real_j = j+3*(numBox%3)
    return(real_i, real_j)

def position_possible(grille, i, j):
    boites = getBoxes(grille)
    chiffres = list(range(1,10))
    #par colonne
    chiffre_possible_colonne = None
    positions_vides = list()
    for row, case in enumerate([l[j] for l in grille]):
        if case == 0 and row != i: positions_vides.append((row, j))
        

    chiffres_possibles_colonne = [c for c in chiffres if c not in [l[j] for l in grille]] #les chiffres possibles dans la ligne
    for chiffre_possible in chiffres_possibles_colonne:
        chiffrePossibleAilleurs = False
        for position in positions_vides:
            if chiffre_possible not in set(grille[position[0]] + [l[j] for l in grille] + boites[int(position[0]/3)*3+int(j/3)]):
                chiffrePossibleAilleurs = True
                break
        if not chiffrePossibleAilleurs: 
            chiffre_possible_colonne = chiffre_possible
            break

    #print(f"par colonne {chiffre_possible_colonne}")

    #par ligne
    chiffre_possible_ligne = None
    positions_vides = list()
    for column, case in enumerate(grille[i]):
        if case == 0 and column != j: positions_vides.append((i, column)) #on recupère les positions vides, sauf celle que l'on cherche

    chiffres_possibles_ligne = [c for c in chiffres if c not in grille[i]] #les chiffres possibles dans la ligne
    for chiffre_possible in chiffres_possibles_ligne:
        chiffrePossibleAilleurs = False
        for position in positions_vides:
            if chiffre_possible not in set(grille[i] + [l[position[1]] for l in grille] + boites[int(i/3)*3+int(position[1]/3)]):
                chiffrePossibleAilleurs = True
                break
        if not chiffrePossibleAilleurs: 
            chiffre_possible_ligne = chiffre_possible
            break

    #print(f"par ligne {chiffre_possible_ligne}")

    #par boite
    chiffre_possible_boite = None
    num_boite = int(i/3)*3+int(j/3)
    boite = getBoxes(grille, True)[num_boite]
    positions_vides = list()
    for index_i in range(len(boite)):
        for index_j, case in enumerate(boite[index_i]):
            bi, bj = getIJFromBox(num_boite, index_i, index_j)
            if case == 0 and (bi != i or bj != j): positions_vides.append((bi, bj))

    chiffres_possibles_box = [c for c in chiffres if c not in addList(boite)] #les chiffres possibles dans la boite
    for chiffre_possible in chiffres_possibles_box:
        chiffrePossibleAilleurs = False
        for position in positions_vides:
            if chiffre_possible not in set(grille[position[0]] + [l[position[1]] for l in grille]):
                chiffrePossibleAilleurs = True
                break
        if not chiffrePossibleAilleurs: 
            chiffre_possible_boite = chiffre_possible
            break

    #print(f"par boite {chiffre_possible_boite}")

    if chiffre_possible_colonne != None: return chiffre_possible_colonne
    elif chiffre_possible_ligne != None: return chiffre_possible_ligne
    elif chiffre_possible_boite != None: return chiffre_possible_boite
    return None
    

grille = [[0, 0, 0, 7, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 3, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 5, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 1, 8],
        [0, 0, 0, 0, 8, 1, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 5, 0],
        [0, 4, 0, 0, 0, 0, 3, 0, 0]]

import time
def solveur_moyen(grille):
    """resoud un sudoku avec la méthode 1 et 2

    Args:
        grille ([[int]]): La grille
    """
    while not est_complete(grille): #tant que la grille n'est pas complète
        pas_de_changement = True
        for i in range(len(grille)):
            for j in range(len(grille[i])):
                if grille[i][j] == 0: #on parcours les cases, et on vérifie que la case est vide
                    position = position_possible(grille, i, j) 
                    if position != None: 
                        pas_de_changement = False
                        grille[i][j] = position #si le nombre de chiffre possible = 1, on le note dans la grille
        print("############################")
        affiche_grille(grille)
        if pas_de_changement: break

affiche_grille(grille)
solveur_moyen(grille)

## Question 6
grille = [
    [0, 0, 0, 0, 0, 7, 0, 9, 0],
    [0, 3, 0, 0, 2, 0, 0, 0, 8],
    [0, 0, 9, 6, 0, 0, 5, 0, 0],
    [0, 0, 5, 3, 0, 0, 9, 0, 0],
    [0, 1, 0, 0, 8, 0, 0, 0, 2],
    [6, 0, 0, 0, 0, 4, 0, 0, 0],
    [3, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 4, 0, 0, 0, 0, 0, 0, 7],
    [0, 0, 7, 0, 0, 0, 3, 0, 0],
]
def solveur_parfait(grille):
    """trouve une solutions au sudoku

    Args:
        grille ([[int]]): La grille

    Returns:
        [[int]]: La solution
    """
    boites = getBoxes(grille)
    for i, ligne in enumerate(grille): #on parcours toutes les cases vides pour les remplirs
        for j, case in enumerate(ligne):
            if case == 0:
                for number in range(1,10):
                    if number not in set(grille[i] + [l[j] for l in grille] +  boites[int(i/3)*3+int(j/3)]): #on test si le numéro est valide
                        grille[i][j] = number
                        new_grille = solveur_parfait(grille)
                        if new_grille and est_complete(new_grille) : return new_grille
                        grille[i][j] = 0
                return None
    return grille

solutions = list()
def solveur_multiple(grille):
    global solutions
    """trouve une solutions au sudoku

    Args:
        grille ([[int]]): La grille

    Returns:
        [[int]]: La solution
    """
    boites = getBoxes(grille)
    for i, ligne in enumerate(grille): #on parcours toutes les cases vides pour les remplirs
        for j, case in enumerate(ligne):
            if case == 0:
                for number in range(1,10):
                    if number not in set(grille[i] + [l[j] for l in grille] +  boites[int(i/3)*3+int(j/3)]): #on test si le numéro est valide
                        grille[i][j] = number
                        new_grille = solveur_multiple(grille)
                        if new_grille and est_complete(new_grille) : solutions.append(new_grille)
                        grille[i][j] = 0
                return None
    return grille
solveur_multiple(grille)
print(len(solutions))

def solveur_parfait(grille):
    """trouve une solutions au sudoku

    Args:
        grille ([[int]]): La grille

    Returns:
        [[int]]: La solution
    """
    boites = getBoxes(grille)
    for i, ligne in enumerate(grille): #on parcours toutes les cases vides pour les remplirs
        for j, case in enumerate(ligne):
            if case == 0:
                for number in range(1,10):
                    if number not in set(grille[i] + [l[j] for l in grille] +  boites[int(i/3)*3+int(j/3)]): #on test si le numéro est valide
                        grille[i][j] = number
                        solveur_parfait(grille)
                        grille[i][j] = 0
                return None
    affiche_grille(grille)
    #print("BOOOOOOOOm")

d = time.time()
solveur_parfait(grille)
print(time.time() - d)

## Question 7
grille = [
    [0, 0, 0, 0, 0, 7, 0, 9, 0],
    [0, 3, 0, 0, 2, 0, 0, 0, 8],
    [0, 0, 9, 6, 0, 0, 5, 0, 0],
    [0, 0, 5, 3, 0, 0, 9, 0, 0],
    [0, 1, 0, 0, 8, 0, 0, 0, 2],
    [6, 0, 0, 0, 0, 4, 0, 0, 0],
    [3, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 4, 0, 0, 0, 0, 0, 0, 7],
    [0, 0, 7, 0, 0, 0, 3, 0, 0],
]

def solveur_moyenV2(grille):
    while not est_complete(grille): #tant que la grille n'est pas complète
        pas_de_changement = True
        for i in range(len(grille)):
            for j in range(len(grille[i])):
                if grille[i][j] == 0: #on parcours les cases, et on vérifie que la case est vide
                    position = position_possible(grille, i, j) 
                    if position != None: 
                        pas_de_changement = False
                        grille[i][j] = position #si le nombre de chiffre possible = 1, on le note dans la grille
        if pas_de_changement: return None
        return grille

solutions = list()
def solveur_multiple(grille):
    global solutions
    boites = getBoxes(grille)
    for i, ligne in enumerate(grille):
        for j, case in enumerate(ligne):
            if case == 0:
                for number in range(1,10):
                    if number not in set(grille[i] + [l[j] for l in grille] +  boites[int(i/3)*3+int(j/3)]): 
                        grille[i][j] = number
                        if est_complete(grille) and grille not in solutions: solutions.append(grille)
                        solveur_multiple(grille)
                        grille[i][j] = 0
    return solutions
    
        
solveur_multiple(grille)
print(len(solutions))

## Question 8

from random import randint
def generateur_sudoku():
    grille = [[0 for _ in range(9)] for _ in range(9)]

    for i in range(len(grille)):
        for j in range(len(grille[0])):
            boites = getBoxes(grille)
            number = randint(0,9)
            if number not in set(grille[i] + [l[j] for l in grille] +  boites[int(i/3)*3+int(j/3)]): grille[i][j] = number
            else: grille[i][j] = 0

    return grille

sudoku = generateur_sudoku()
affiche_grille(sudoku)
solveur_moyen(sudoku)

def generateur_sudoku():
    global solutions

    #Génération d'un début de grille avec n valeur
    n = 5
    grille = [[0 for _ in range(9)] for _ in range(9)]

    numbers = [randint(1,9) for _ in range(n)]
    for number in numbers:
        boites = getBoxes(grille)
        i = randint(0,8)
        j = randint(0,8)
        while number in set(grille[i] + [l[j] for l in grille] +  boites[int(i/3)*3+int(j/3)]):
            i = randint(0,8)
            j = randint(0,8)
        grille[i][j] = number
    
    grille = solveur_parfait(grille) # on complète la grille avec le solveur parfait

    solutions = list()
    solveur_multiple(grille)
    while len(solutions) > 1 or len(solutions) == 0:
        solutions = list()
        print(len(solutions))
        i = randint(0,8)
        j = randint(0,8)
        grille[i][j] = 0
        affiche_grille(grille)
        time.sleep(1)
        solveur_multiple(grille)





            

    

