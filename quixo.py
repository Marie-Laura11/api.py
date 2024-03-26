"""
Ce module contient les mécaniques du jeu Quixo. Il contient les fonctions 
qui permettent d'afficher le jeu, de demander un coup à l'utilisateur ainsi 
que d'analyser les paramètres de la ligne de commande.
"""


def formater_legende(joueurs):
    """
    Fonction qui accepte en argument la même liste de joueurs que celle retournée 
    par le serveur de jeu et retourne la légende correspondante en art ASCII (chaîne de caractères). 
    """
    if len(joueurs) == 2:
        return f"Légende: X={joueurs[0]}, O={joueurs[1]}"
    else:
        return "Légende: Impossible de formater la légende avec le nombre de joueurs donné."
