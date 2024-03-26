"""Module api"""

import requests

def lister_parties(idul, secret):
    """
    Fonction qui accepte en entrée un nom d'usager (idul) et le jeton 
    qui lui est associé (secret), et qui retourne en sortie la liste des 
    parties reçues du serveur, après avoir décodé le JSON de sa réponse.
    """
    base_url = 'https://pax.ulaval.ca/quixo/api/h24/'
    try:
        response = requests.get(base_url + 'parties', auth=(idul, secret), timeout=3)
        response.raise_for_status()
        data = response.json()
        return data.get('parties', [])
    except requests.exceptions.HTTPError as ex:
        data = ex.response.json()
        if ex.response.status_code == 401:
            raise PermissionError(data.get('message', 'Unauthorized')) from ex
        elif ex.response.status_code == 406:
            raise RuntimeError(data.get('message', 'Not Acceptable')) from ex
        else:
            raise ConnectionError(f"HTTP Error: {ex.response.status_code}") from ex
    except Exception as ex:
        raise ConnectionError(f"Connection Error: {str(ex)}") from ex

def recuperer_partie(id_partie, idul, secret):
    """
    Fontion qui accepte en entrée un identifiant de partie (id_partie) sous la 
    forme d'une chaîne de caractères ainsi qu'un nom d'usager (idul) et le jeton 
    qui lui est associé (secret), et qui retourne en sortie un tuple de quatre (4) 
    éléments constitué de l'identifiant de la partie, de la liste des joueurs, de l'état 
    du plateau et du vainqueur retourné par le serveur. 
    """
    base_url = 'https://pax.ulaval.ca/quixo/api/h24/'
    try:
        response = requests.post(base_url + id_partie, auth=(idul, secret), timeout=3)
        response.raise_for_status()
        data = response.json()
        partie_id = data.get('id')
        joueurs = data.get('état').get('joueurs')
        plateau = data.get('état').get('plateau')
        vainqueur = data.get('gagnant')
        return partie_id, joueurs, plateau, vainqueur
    except requests.exceptions.HTTPError as ex:
        data = ex.response.json()
        if ex.response.status_code == 401:
            raise PermissionError(data.get('message', 'Unauthorized')) from ex
        elif ex.response.status_code == 406:
            raise RuntimeError(data.get('message', 'Not Acceptable')) from ex
        else:
            raise ConnectionError(f"HTTP Error: {ex.response.status_code}") from ex
    except Exception as ex:
        raise ConnectionError(f"Connection Error: {str(ex)}") from ex

def debuter_partie(idul, secret):
    """
    Fontion qui accepte en entrée un nom d'usager (idul) et le jeton qui 
    lui est associé (secret), et qui retourne en sortie un tuple de trois 
    (3) éléments constitué de l'identifiant de la partie, de la liste des 
    joueurs et de l'état du plateau. 
    """
    base_url = 'https://pax.ulaval.ca/quixo/api/h24/'
    try:
        response = requests.put(base_url, auth=(idul, secret), timeout=3)
        response.raise_for_status()
        data = response.json()
        partie_id = data.get('id')
        joueurs = data.get('état').get('joueurs')
        plateau = data.get('état').get('plateau')
        return partie_id, joueurs, plateau
    except requests.exceptions.HTTPError as ex:
        data = ex.response.json()
        if ex.response.status_code == 401:
            raise PermissionError(data.get('message', 'Unauthorized')) from ex
        elif ex.response.status_code == 406:
            raise RuntimeError(data.get('message', 'Not Acceptable')) from ex
        else:
            raise ConnectionError(f"HTTP Error: {ex.response.status_code}") from ex
    except Exception as ex:
        raise ConnectionError(f"Connection Error: {str(ex)}") from ex

def jouer_coup(id_partie, origine, direction, idul, secret):
    """
    Fonction qui accepte en entrée les cinq (5) arguments id_partie, origine, direction, 
    idul et secret, et qui retourne en sortie un tuple de trois (3) éléments constitué de 
    l'identifiant de la partie, de la liste des joueurs et de l'état du plateau. 
    """
    base_url = 'https://pax.ulaval.ca/quixo/api/h24/jouer/'
    try:
        response = requests.put(base_url, auth=(idul, secret), json={
            "id": id_partie,
            "origine": origine,
            "direction": direction
        }, timeout=3)
        response.raise_for_status()  # Lève une exception pour les codes de statut HTTP >= 400
        data = response.json()
        partie_id = data.get('id')
        joueurs = data.get('état').get('joueurs')
        plateau = data.get('état').get('plateau')
        gagnant = data.get('gagnant')
        if gagnant:
            raise StopIteration(gagnant)
        return partie_id, joueurs, plateau
    except requests.exceptions.HTTPError as ex:
        data = ex.response.json()
        if ex.response.status_code == 401:
            raise PermissionError(data.get('message', 'Unauthorized')) from ex
        elif ex.response.status_code == 406:
            raise RuntimeError(data.get('message', 'Not Acceptable')) from ex
        else:
            raise ConnectionError(f"HTTP Error: {ex.response.status_code}") from ex
    except Exception as ex:
        raise ConnectionError(f"Connection Error: {str(ex)}") from ex
