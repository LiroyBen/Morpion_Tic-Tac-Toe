def init_tableau():
    tableau = ['0', '1', '2','3', '4', '5','6', '7', '8']
    return tableau

def affichagetableau(tableau):
    print(tableau[0],'|', tableau[1],'|', tableau[2])
    print('--+---+--')
    print(tableau[3],'|', tableau[4],'|', tableau[5])
    print('--+---+--')
    print(tableau[6],'|', tableau[7],'|', tableau[8])

def jouer(x_or_o, Joueur, tableau):
    print("\nAu joueur", Joueur, "de jouer !")
    print ("Vous possèdez les", x_or_o + ("."))
    reponse = (input('Sur quelle casse vous voulez jouer ? : '))
    reponsecheck = not_good_caractere(reponse)
    reponse = int(reponsecheck)
    while (tableau[reponse - 1] == ('X') or tableau[reponse - 1] == ('O')):
        print("Oups, cette casse est déjà jouée !")
        reponse = input('Sur quelle casse vous voulez jouer ? : ')
        reponsecheck = not_good_caractere(reponse)
        reponse = int(reponsecheck)
    tableau[reponse - 1] = x_or_o
    return tableau

def not_good_caractere(reponse):
    while not (len(reponse) <= 1 and reponse >= chr(48) and reponse <= chr(57) and reponse != chr(48)):
        reponse = (input("Oups, ce(s) caractère(s) n'est(ne sont) pas accepté ! Ressayez !"))
    return reponse

def wining(gagnant, tableau):
    if tableau[0] == tableau[1] and tableau[1] == tableau[2] or tableau[3] == tableau[4] and tableau[4] == tableau[5] or tableau[6] == tableau[7] and tableau[7] == tableau[8] or tableau[0] == tableau[3] and tableau[3] == tableau[6]  or tableau[1] == tableau[4] and tableau[4] == tableau[7] or tableau[2] == tableau[5] and tableau[5] == tableau[8] or tableau[0] == tableau[4] and tableau[4] == tableau[8] or tableau[2] == tableau[4] and tableau[4] == tableau[6]:
        print ("Le joueur", gagnant, "à gagné la partie !" )
        return True
    return False

def no_name_enter(joueur_not_enter):
    while not joueur_not_enter:
        joueur_not_enter = str(input("Vous devez entrer un pseudo !"))
    return joueur_not_enter


def start():
    tableau = init_tableau()
    tours = 0
    print ("##################################################")
    print ("#                                                #")
    print ("# ##   ##   ####   ###   ###  ###   ####   ##  # #")
    print ("# # # # #  #    #  # #   # #   #   #    #  # # # #")
    print ("# #  #  #  #    #  ###   ###   #   #    #  #  ## #")
    print ("# #     #   ####   #  #  #    ###   ####   #   # #")
    print ("#                                                #")
    print ("#    ","1PROG - Supinfo | Made By Liroy Benaim","    #")
    print ("##################################################\n")
    Joueur1 = str(input("Qu'elle est le pseudo du premier Joueur ? : "))
    Joueur1 = no_name_enter(Joueur1)
    Joueur2 = str(input("Merci, et celui du deuxième Joueur ? : "))
    Joueur2 = no_name_enter(Joueur2)
    while Joueur1.lower()==Joueur2.lower():
        print ("Les deux joueurs ne peuvent pas avoir le même pseudo !")
        Joueur1 = str(input("Qu'elle est le pseudo du premier Joueur ? : "))
        Joueur1 = no_name_enter(Joueur1)
        Joueur2 = str(input("Qu'elle est le pseudo du deuxième Joueur ? : "))
        Joueur2 = no_name_enter(Joueur2)
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
        if (wining(gagnant, tableau)):
            break

        tours = tours + 1
        if (tours== 9):
            affichagetableau(tableau)
            print('\nOups, Match Nul !')
            break

start()
reponse = str(input("Souhaitez-vous faire une nouvelle partie ? (oui/non): "))
while not (reponse.lower() == "oui" or reponse.lower() == "non" or reponse.lower() == "yes" or reponse.lower() == "no" or reponse.lower() == "y" or reponse.lower() == "n" or reponse.lower() == "o"):
  reponse = str(input("Vous devez répondre par Oui ou Non ! "))
if (reponse.lower() == "non" or reponse.lower() == "n" or reponse.lower() == "no"):
    print("Merci d'avoir joué ! A bientôt !")
    exit = input("Appuiez sur <entrée> pour quitter.")
while (reponse.lower() == "oui" or reponse.lower() == "yes" or reponse.lower() == "o" or reponse.lower() == "y"):
    start()
    reponse = str(input("Souhaitez-vous faire une nouvelle partie ? (oui/non): "))