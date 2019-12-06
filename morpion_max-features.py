import os
from colorama import *
init(autoreset=True)

def init_tableau():
    tableau = ['1', '2', '3','4', '5', '6','7', '8', '9']
    return tableau

def affichagetableau(tableau):
    print(tableau[0],Fore.YELLOW + '|', tableau[1],Fore.YELLOW + '|', tableau[2])
    print(Fore.YELLOW + '--+---+--')
    print(tableau[3],Fore.YELLOW + '|', tableau[4],Fore.YELLOW + '|', tableau[5])
    print(Fore.YELLOW + '--+---+--')
    print(tableau[6],Fore.YELLOW + '|', tableau[7],Fore.YELLOW + '|', tableau[8])

def jouer(x_or_o, Joueur, tableau):
    print("\nAu joueur", Joueur, "de jouer !")
    print ("Vous possèdez les", x_or_o + (Fore.WHITE + "."))
    reponse = (input('Sur quelle casse vous voulez jouer ? : '))
    reponsecheck = not_good_caractere(reponse)
    reponse = int(reponsecheck)
    while (tableau[reponse - 1] == (Fore.RED + 'X') or tableau[reponse - 1] == (Fore.GREEN + 'O')):
        print(Fore.RED + "Oups, cette casse est déjà jouée !")
        reponse = input('Sur quelle casse vous voulez jouer ? : ')
        reponsecheck = not_good_caractere(reponse)
        reponse = int(reponsecheck)
    os.system("cls")
    tableau[reponse - 1] = x_or_o
    return tableau

def not_good_caractere(reponse):
    while not (len(reponse) <= 1 and reponse >= chr(48) and reponse <= chr(57) and reponse != chr(48)):
        print(Fore.RED + "Oups, ce(s) caractère(s) n'est(ne sont) pas accepté ! Ressayez !")
        reponse = (input())
    return reponse

def wining(gagnant, tableau):
    if tableau[0] == tableau[1] and tableau[1] == tableau[2] or tableau[3] == tableau[4] and tableau[4] == tableau[5] or tableau[6] == tableau[7] and tableau[7] == tableau[8] or tableau[0] == tableau[3] and tableau[3] == tableau[6]  or tableau[1] == tableau[4] and tableau[4] == tableau[7] or tableau[2] == tableau[5] and tableau[5] == tableau[8] or tableau[0] == tableau[4] and tableau[4] == tableau[8] or tableau[2] == tableau[4] and tableau[4] == tableau[6]:
        print (Fore.GREEN + "Le joueur", gagnant, Fore.GREEN + "à gagné la partie !" )
        return True
    return False

def no_name_enter(joueur_not_enter):
    while not joueur_not_enter:
        print(Fore.RED + "Vous devez entrer un pseudo !")
        joueur_not_enter = str(input())
    return joueur_not_enter


def start():
    tableau = init_tableau()
    tours = 0
    print (Fore.GREEN + "##################################################")
    print (Fore.GREEN + "#                                                #")
    print (Fore.GREEN + "# ##   ##   ####   ###   ###  ###   ####   ##  # #")
    print (Fore.GREEN + "# # # # #  #    #  # #   # #   #   #    #  # # # #")
    print (Fore.GREEN + "# #  #  #  #    #  ###   ###   #   #    #  #  ## #")
    print (Fore.GREEN + "# #     #   ####   #  #  #    ###   ####   #   # #")
    print (Fore.GREEN + "#                                                #")
    print (Fore.GREEN + "#    ",Fore.RED + "1PROG - Supinfo | Made By Liroy Benaim",Fore.GREEN + "    #")
    print (Fore.GREEN + "##################################################\n")
    print (Fore.MAGENTA + "Qu'elle est le pseudo du premier Joueur ? ")
    Joueur1 = str(input())
    Joueur1 = no_name_enter(Joueur1)
    os.system("cls")
    print (Fore.CYAN + "Merci, et celui du deuxième Joueur ? ")
    Joueur2 = str(input())
    Joueur2 = no_name_enter(Joueur2)
    os.system("cls")
    while Joueur1.lower()==Joueur2.lower():
        os.system("cls")
        print (Fore.RED + "Les deux joueurs ne peuvent pas avoir le même pseudo !")
        print (Fore.MAGENTA +"Qu'elle est le pseudo du premier Joueur ? ")
        Joueur1 = str(input())
        Joueur1 = no_name_enter(Joueur1)
        print (Fore.CYAN + "Qu'elle est le pseudo du deuxième Joueur ? ")
        Joueur2 = str(input())
        Joueur2 = no_name_enter(Joueur2)
        os.system("cls")
    print (Fore.GREEN + "C'est Parti ! Bon Jeu !")
    Joueur = Joueur1
    while True: 
        affichagetableau(tableau)
        if Joueur == Joueur1: 
            jouer(Fore.RED + "X", Fore.RED + Joueur, tableau)
            gagnant = Joueur
            Joueur = Joueur2
        else:
            jouer(Fore.GREEN + "O", Fore.GREEN + Joueur, tableau)
            gagnant = Joueur
            Joueur = Joueur1
        if (wining(gagnant, tableau)):
            break

        tours = tours + 1
        if (tours== 9):
            affichagetableau(tableau)
            print(Fore.RED + '\nOups, Match Nul !')
            break

os.system("cls")
start()
reponse = str(input("Souhaitez-vous faire une nouvelle partie ? (oui/non): "))
os.system("cls")
while not (reponse.lower() == "oui" or reponse.lower() == "non" or reponse.lower() == "yes" or reponse.lower() == "no" or reponse.lower() == "y" or reponse.lower() == "n" or reponse.lower() == "o"):
  print(Fore.RED + "Vous devez répondre par Oui ou Non !")
  reponse = str(input())
  os.system("cls")
if (reponse.lower() == "non" or reponse.lower() == "n" or reponse.lower() == "no"):
    print(Fore.GREEN + "Merci d'avoir joué ! A bientôt !")
    exit = input("Appuiez sur <entrée> pour quitter.")
while (reponse.lower() == "oui" or reponse.lower() == "yes" or reponse.lower() == "o" or reponse.lower() == "y"):
    start()
    reponse = str(input("Souhaitez-vous faire une nouvelle partie ? (oui/non): "))