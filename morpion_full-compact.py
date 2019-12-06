def init_tableau():
    tableau = ['1', '2', '3','4', '5', '6','7', '8', '9']
    return tableau

def affichagetableau(tableau):
    print(tableau[0],'|', tableau[1], '|', tableau[2])
    print( '--+---+--')
    print(tableau[3], '|', tableau[4], '|', tableau[5])
    print( '--+---+--')
    print(tableau[6], '|', tableau[7], '|', tableau[8])

def jouer(x_or_o, Joueur, tableau):
    print("\nAu joueur", Joueur, "de jouer !")
    print ("Vous possèdez les", x_or_o + ".")
    reponse = int(input('Sur quelle casse vous voulez joué ? : '))
    while (reponse <= 0 or reponse >= 10):
        print("Vous devez une casse comprise entre 1 et 9 !")
        reponse = int(input('Sur quelle casse vous voulez joué ? : '))
    while (tableau[reponse - 1] == 'X' or tableau[reponse - 1] == 'O'):
        print("Oups, cette case est déjà joué !")
        reponse = int(input('Sur quelle casse vous voulez joué ? : '))
    tableau[reponse - 1] = x_or_o
    return tableau

def gagne(gagnant, tableau):
    if tableau[0] == tableau[1] and tableau[1] == tableau[2] or tableau[3] == tableau[4] and tableau[4] == tableau[5] or tableau[6] == tableau[7] and tableau[7] == tableau[8] or tableau[0] == tableau[3] and tableau[3] == tableau[6]  or tableau[1] == tableau[4] and tableau[4] == tableau[7] or tableau[2] == tableau[5] and tableau[5] == tableau[8] or tableau[0] == tableau[4] and tableau[4] == tableau[8] or tableau[2] == tableau[4] and tableau[4] == tableau[6]:
        print ("Le joueur", gagnant, "à gagné la partie !" )
        return True
    return False

def start():
    tableau = init_tableau()
    tours = 0
    Joueur1 = str(input("Qu'elle est le prénom du premier Joueur ? "))
    Joueur2 = str(input("Merci, et celui du deuxième Joueur ? "))
    print ("C'est Parti ! Bon Jeu !")
    Joueur = Joueur1
    while True: 
        affichagetableau(tableau)
        if Joueur == Joueur1: 
            jouer("X", Joueur, tableau)
            gagnant = Joueur
            Joueur = Joueur2
        else:
            jouer("O", Joueur, tableau)
            gagnant = Joueur
            Joueur = Joueur1
        if (gagne(gagnant, tableau)):
            break

        tours = tours + 1
        if (tours== 9):
            affichagetableau(tableau)
            print('\nOups, Match Nul !')
            break

start()
reponse = str(input("Souhaitez-vous faire une nouvelle partie ? (oui/non): "))
if reponse.lower() == "non":
    print("Merci d'avoir joué ! A bientôt !")
while (reponse.lower() == "oui"):
    start()
    reponse = str(input("Souhaitez-vous faire une nouvelle partie ? (oui/non): "))