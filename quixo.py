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

def formater_plateau(plateau):
    """
    Fonction qui accepte en argument l'état du plateau (tel que représenté par la valeur de la clé 
    plateau de l'état de jeu ci-dessous) et qui retourne le plateau correspondant 
    en art ASCII (chaîne de caractères).
    """
    formatted_board = "   -------------------\n"
    for i, row in enumerate(plateau):
        formatted_board += f"{i + 1} | "
        for cell in row:
            formatted_board += f" {cell} |"
        formatted_board += "\n"
        if i < len(plateau) - 1:
            formatted_board += "  |---|---|---|---|---|\n"
    formatted_board += "--|---|---|---|---|---\n"
    formatted_board += "  | 1   2   3   4   5\n"
    return formatted_board

def formater_jeu(joueurs, plateau):
    """
    Fonction qui accepte en argument la liste de joueurs et l'état du plateau et qui, 
    à l'aide des deux fonctions précédentes, retourne le plateau correspondant 
    en art ASCII (chaîne de caractères).
    """
    legende = formater_legende(joueurs)
    plateau_formate = formater_plateau(plateau)
    jeu_formate = f"{legende}\n{plateau_formate}"
    return jeu_formate

def formater_les_parties(parties):
    """
    Fonction qui accepte en argument une liste de parties sous forme de dictionnaires 
    """
