def ex1a():
    somme = 0
    for k in range (101):
        somme = somme + k**2
    print(somme)

def ex1b():
    somme = 0
    k = 0
    while k <= 100:
        somme = somme + k**2
        k = k + 1
    print(somme)

def ex2():
    mdp = "coucou"
    reponse = ""
    k = 3
    while k > 0:
        print("Vous avez ", k, " essais restants")
        reponse  = input("Entrez le mot de passe")

        if(mdp == reponse):
            print ("Mot de passe correct")
            k = -1

        else:
            print("Mot de passe Incorrect ")
            k = k - 1
        if(k == 5):
            print ("Vous pouvez entrer")
        if (k == 0):
            print("Vous n'avez plus de tentatives")
