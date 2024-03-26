"""Module api"""

import requests

def lister_parties(idul, secret):
    """
    Fonction qui accepte en entrée un nom d'usager (idul) et le jeton 
    qui lui est associé (secret), et qui retourne en sortie la liste des 
    parties reçues du serveur, après avoir décodé le JSON de sa réponse.
    """
    base_url = 'https://pax.ulaval.ca/quixo/api/h24/'
