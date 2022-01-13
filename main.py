import random


def demander_mode():
    print("Mode facile : Nombre maximum = 10")
    print("Mode moyen : Nombre maximum = 25")
    print("Mode difficile : Nombre maximum = 50")
    print("Mode expert : Nombre maximum = 100")
    print("Mode impossible : Nombre maximum = 999")
    print("Mode battle : La personne qui a le meilleur score gagne. (Nombre maximum = 20)")
    print()
    mode_str = input("Voulez-vous jouer en mode facile (1), moyen (2), difficile (3), expert (4), impossible (5), libre (6) ou battle (7) ? ")
    mode_int = 10
    while mode_int == 10:
        try:
           mode_int = int(mode_str)
        except:
            print("ERREUR: Vous devez rentrer un chiffre entre 1 et 7.")
            mode_int = 10
            print()
            mode_str = input("Voulez-vous jouer en mode facile (1), moyen (2), difficile (3), expert (4), impossible (5), libre (6) ou battle (7) ? ")
        else:
            if mode_int < 1:
                print("ERREUR: Vous devez rentrer un chiffre entre 1 et 7.")
                mode_int = 10
                print()
                mode_str = input("Voulez-vous jouer en mode facile (1), moyen (2), difficile (3), expert (4), impossible (5), libre (6) ou battle (7) ? ")
            elif mode_int > 7:
                print("ERREUR: Vous devez rentrer un chiffre entre 1 et 7.")
                mode_int = 10
                print()
                mode_str = input("Voulez-vous jouer en mode facile (1), moyen (2), difficile (3), expert (4), impossible (5), libre (6) ou battle (7) ? ")
    if mode_int == 0:
        print("Le nombre maximum est 10.")
    elif mode_int == 1:
        print("Le nombre maximum est 25.")
    elif mode_int == 2:
        print("Le nombre maximum est 50.")
    elif mode_int == 3:
        print("Le nombre maximum est 100.")
    elif mode_int == 4:
        print("Le nombre maximum est 999.")
    elif mode_int == 6:
        print("Le nombre maximum est 20.")
    print()
    return mode_int


def demander_nb_personnes():
    global mode
    nb_personnes_int = 0
    if mode == 7:
        while nb_personnes_int == 0:
            nb_personnes_str = input("Combien de personnes vont jouer ? ")
            try:
                nb_personnes_int = int(nb_personnes_str)
            except:
                print("ERREUR: Vous devez rentrer un nombre pour le nombre de joueurs.")
                print()
        if nb_personnes_int < 2:
            print("ERREUR: Le nombre de joueurs ne doit pas ếtre en dessous de 2. Réessayez.")
            print()
            nb_personnes_int = 0
    print()
    return nb_personnes_int


def demander_nom():
    nomlist = []
    nom_str = ""
    reponse = ""
    if mode == 7:
        for i in range(0, NB_PERSONNES):
            nom_str = input(f"Quel est votre nom Joueur {i + 1} ? ")
            while nom_str == "":
                print("ERREUR: Vous devez entrer un nom valide.")
                print()
                nom_str = input(f"Quel est votre nom Joueur {i + 1} ? ")
            while reponse == "":
                reponse = input(f'"{nom_str}" est bien le nom que vous choisissez ? (oui/non) ')
                print()
                if reponse == "oui":
                    print(f'"{nom_str}" est bien votre nom.')
                elif reponse == "non":
                    nom_str = input(f"Quel est votre nom Joueur {i + 1} ? ")
                    reponse = ""
                    print()
                elif not reponse == "oui" or "non":
                    print('ERREUR: Vous devez rentrer "oui" ou "non". Réessayez.')
                    reponse = ""
                    print()
            nomlist.append(nom_str)
            print()
            reponse = ""
            i = i + 1
        return nomlist


def start():
    global nom
    nb_points = 0
    if not mode == 7:
        for i in range(0, NB_QUESTIONS):
            print(f"Question n°{i + 1} sur {NB_QUESTIONS}:")
            if poser_question():
                print("Réponse correcte.")
                nb_points += 1
            else:
                print("Réponse incorrecte.")
            print()
        print(f"Votre note est : {nb_points} / {NB_QUESTIONS}.")
        moyenne = int(NB_QUESTIONS / 2)
        if nb_points == NB_QUESTIONS:
            print("Excellent !")
        elif nb_points == 0:
            print("Révisez vos maths !")
        elif nb_points == moyenne:
            print("Juste la moyenne !")
        elif nb_points > moyenne:
            print("Pas mal !")
        else:
            print("Peut mieux faire !")
        print()

    else:
        scorelist = []
        n = -1
        for i in range(0, NB_PERSONNES):
            i += 1
            print(f"Questions pour {nom[n+1]} :")
            print()
            n = n + 1
            for i in range(0, NB_QUESTIONS):
                print(f"Question n°{i + 1} sur {NB_QUESTIONS}:")
                if poser_question():
                    print("Réponse correcte.")
                    nb_points += 1
                else:
                    print("Réponse incorrecte.")
                print()
            print(f"Votre note est : {nb_points} / {NB_QUESTIONS}.")
            moyenne = int(NB_QUESTIONS / 2)
            if nb_points == NB_QUESTIONS:
                print("Excellent !")
            elif nb_points == 0:
                print("Révisez vos maths !")
            elif nb_points == moyenne:
                print("Juste la moyenne !")
            elif nb_points > moyenne:
                print("Pas mal !")
            else:
                print("Peut mieux faire !")
            print()
            scorelist.append(nb_points)
            nb_points = 0
        infos = zip(nom, scorelist)
        infos_list = list(infos)
        infos_list.sort(key=lambda x: x[1], reverse=True)
        gagnant = infos_list[0]
        nom_gagnant = gagnant[0]
        score_gagnant = gagnant[1]
        nb = 1
        infos_j = infos_list[nb]
        print("Voici le classement :")
        print()
        print(f"{nom_gagnant} gagne avec un score de {score_gagnant} points. Bravo !")
        print()
        if NB_PERSONNES == 2:
            for i in range(2, NB_PERSONNES):
                nom_j = infos_j[0]
                score_j = infos_j[1]
                print(f"{nom_j} termine à la {i}e place avec un score de {score_j} points.")
                i = i + 1
                print()
        else:
            for i in range(1, NB_PERSONNES):
                nom_j = infos_j[0]
                score_j = infos_j[1]
                print(f"{nom_j} termine à la {i+1}e place avec un score de {score_j} points.")
                if not nb == NB_PERSONNES-1:
                    nb = nb + 1
                    infos_j = infos_list[nb]
                i = i + 1
                print()

"""for i in range(1, NB_PERSONNES):
    while not i == NB_PERSONNES:
        if list score[] == list score[]:
        print(...)"""


def demander_difficulte(n_diff_str="5"):
    print("a = additions")
    print("s = soustractions")
    print("m = multiplications")
    print("d = divisions")
    print()
    print("Mode 1 = additions")
    print("Mode 2 = soustractions")
    print("Mode 3 = multiplications")
    print("Mode 4 = divisions")
    print("Mode 5 = a/s/m/d")
    print("Mode 6 = a/s/m")
    print("Mode 7 = a/s/d")
    print("Mode 8 = a/m/d")
    print("Mode 9 = s/m/d")
    print("Mode 10 = a/s")
    print("Mode 11 = a/m")
    print("Mode 12 = a/d")
    print("Mode 13 = s/m")
    print("Mode 14 = s/d")
    print("Mode 15 = m/d")
    print()

    n_diff_str = input("Quel mode souhaitez-vous ? (Vous devez entrer un nombre) : ")
    n_diff_int = 0
    while n_diff_int == 0:
        try:
            n_diff_int = int(n_diff_str)
        except:
            print("ERREUR: Vous devez rentrer un chiffre entre 1 et 15.")
            n_diff_int = 0
            print()
            n_diff_str = input("Quel mode souhaitez-vous ? (Vous devez entrer un nombre) : ")
        else:
            if n_diff_int < 1:
                print("ERREUR: Vous devez rentrer un chiffre entre 1 et 15.")
                n_diff_int = 0
                print()
                n_diff_str = input("Quel mode souhaitez-vous ? (Vous devez entrer un nombre) : ")
            elif n_diff_int > 15:
                print("ERREUR: Vous devez rentrer un chiffre entre 1 et 15.")
                n_diff_int = 0
                print()
                n_diff_str = input("Quel mode souhaitez-vous ? (Vous devez entrer un nombre) : ")
    print()
    return n_diff_int


def demander_nb_max():
    nb_max_int = 0
    while nb_max_int == 0:
        nb_max_str = input("Quel nombre maximum voulez-vous dans les opérations ? ")
        try:
            nb_max_int = int(nb_max_str)
        except:
            print("ERREUR: Vous devez rentrer un nombre. Réessayez.")
            print()
        else:
            if nb_max_int < 10:
                print("ERREUR: Le nombre ne doit pas être en dessous de 10. Réessayez.")
                nb_max_int = 0
                print()
    return nb_max_int


def demander_nb_questions():
    nb_questions_int = 0
    while nb_questions_int == 0:
        nb_questions_str = input("Combien de questions voulez-vous ? ")
        try:
            nb_questions_int = int(nb_questions_str)
        except:
            print("ERREUR: Vous devez rentrer un nombre. Réessayez.")
            print()
        else:
            if nb_questions_int < 4:
                print("ERREUR: Le nombre ne doit pas être en dessous de 4. Réessayez.")
                print()
                nb_questions_int = 0
    print()
    return nb_questions_int


def poser_question():
    global diff
    a = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    b = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    o = random.randint(0, 3)
    operateur_str = "+"

    if diff == 1:
        operateur_str = "+"

    elif diff == 2:
        operateur_str = "-"

    elif diff == 3:
        operateur_str = "×"

    elif diff == 4:
        operateur_str = "/"

    elif diff == 5:
        if o == 1:
            operateur_str = "-"
        elif o == 2:
            operateur_str = "×"
        elif o == 3:
            operateur_str = "/"

    elif diff == 6:
        o = random.randint(0, 2)
        if o == 1:
            operateur_str = "-"
        elif o == 2:
            operateur_str = "×"

    elif diff == 7:
        o = random.randint(0, 2)
        if o == 1:
            operateur_str = "-"
        elif o == 2:
            operateur_str = "/"

    elif diff == 8:
        o = random.randint(0, 2)
        if o == 1:
            operateur_str = "×"
        elif o == 2:
            operateur_str = "/"

    elif diff == 9:
        o = random.randint(0, 2)
        if o == 0:
            operateur_str = "-"
        elif o == 1:
            operateur_str = "×"
        elif o == 2:
            operateur_str = "/"

    elif diff == 10:
        o = random.randint(0, 1)
        if o == 0:
            operateur_str = "+"
        elif o == 1:
            operateur_str = "-"

    elif diff == 11:
        o = random.randint(0, 1)
        if o == 0:
            operateur_str = "+"
        elif o == 1:
            operateur_str = "×"

    elif diff == 12:
        o = random.randint(0, 1)
        if o == 0:
            operateur_str = "+"
        elif o == 1:
            operateur_str = "/"

    elif diff == 13:
        o = random.randint(0, 1)
        if o == 0:
            operateur_str = "-"
        elif o == 1:
            operateur_str = "×"

    elif diff == 14:
        o = random.randint(0, 1)
        if o == 0:
            operateur_str = "-"
        elif o == 1:
            operateur_str = "/"

    elif diff == 15:
        o = random.randint(0, 1)
        if o == 0:
            operateur_str = "×"
        elif o == 1:
            operateur_str = "/"

    reponse_int = -1000
    while reponse_int == -1000:
        reponse_str = input(f"Calculez : {a} {operateur_str} {b} = ")
        try:
            reponse_int = int(reponse_str)
        except:
            print(f"ERREUR: Vous devez rentrer un nombre.")
            print()
    calcul = a+b

    if diff == 1:
        calcul = a+b

    elif diff == 2:
        calcul = a-b

    elif diff == 3:
        calcul = a*b

    elif diff == 4:
        calcul = a/b

    elif diff == 5:
        if o == 0:
            calcul = a+b
        elif o == 1:
            calcul = a-b
        elif o == 2:
            calcul = a*b
        elif o == 3:
            calcul = a/b

    elif diff == 6:
        if o == 0:
            calcul = a+b
        elif o == 1:
            calcul = a-b
        elif o == 2:
            calcul = a*b

    elif diff == 7:
        if o == 0:
            calcul = a+b
        elif o == 1:
            calcul = a-b
        elif o == 2:
            calcul = a/b

    elif diff == 8:
        if o == 0:
            calcul = a+b
        elif o == 1:
            calcul = a*b
        elif o == 2:
            calcul = a/b

    elif diff == 9:
        if o == 0:
            calcul = a-b
        elif o == 1:
            calcul = a*b
        elif o == 2:
            calcul = a/b

    elif diff == 10:
        if o == 0:
            calcul = a+b
        elif o == 1:
            calcul = a-b

    elif diff == 11:
        if o == 0:
            calcul = a+b
        elif o == 1:
            calcul = a*b

    elif diff == 12:
        if o == 0:
            calcul = a+b
        elif o == 1:
            calcul = a/b

    elif diff == 13:
        if o == 0:
            calcul = a-b
        elif o == 1:
            calcul = a*b

    elif diff == 14:
        if o == 0:
            calcul = a-b
        elif o == 1:
            calcul = a/b

    elif diff == 15:
        if o == 0:
            calcul = a*b
        elif o == 1:
            calcul = a/b

    if reponse_int == calcul:
        return True
    print(f"La réponse était {calcul}.")
    return False


def nouvel_essai():
    nouvel_essai = ""
    while nouvel_essai == "":
        nouvel_essai = input("Voulez-vous réessayer ? (oui/non) ")
        if nouvel_essai == "oui":
            print()
            demander_mode()
            demander_nb_personnes()
            demander_nom()
            demander_difficulte(n_diff_str="5")
            demander_nb_questions()
            start()
        elif nouvel_essai == "non":
            quit()
        elif not nouvel_essai == "oui" or "non":
            print('ERREUR: Vous devez rentrer "oui" ou "non". Réessayez.')
            nouvel_essai = ""
            print()


mode = demander_mode()
NB_PERSONNES = demander_nb_personnes()
nom = demander_nom()

NOMBRE_MAX = 0
if mode == 1:
    NOMBRE_MAX = 10
elif mode == 2:
    NOMBRE_MAX = 25
elif mode == 3:
    NOMBRE_MAX = 50
elif mode == 4:
    NOMBRE_MAX = 100
elif mode == 5:
    NOMBRE_MAX = 999
elif mode == 6:
    NOMBRE_MAX = demander_nb_max()
elif mode == 7:
    NOMBRE_MAX = 20

diff = demander_difficulte(n_diff_str="5")
NOMBRE_MIN = 1
NB_QUESTIONS = demander_nb_questions()
start()
nouvel_essai()