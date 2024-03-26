"""
Module principal
"""
import quixo
import api

def main():
    """
    Fonction qui fait démarrer les parties
    """
    idul_du_joueur = input("Entrez l'IDUL du joueur : ")
    secret = input("Entrez le jeton personnel du joueur : ")

    try:

        id_partie, joueurs, plateau = api.debuter_partie(idul_du_joueur, secret)

        while True:
            print(quixo.formater_jeu(joueurs, plateau))
            origine, direction = quixo.recuperer_le_coup()
            id_partie, joueurs, plateau = api.jouer_coup(id_partie, origine, direction,
                                                         idul_du_joueur, secret)

    except (ConnectionError, PermissionError, RuntimeError) as ex:
        print("Une erreur est survenue:", str(ex))

if __name__ == "__main__":
    main()
