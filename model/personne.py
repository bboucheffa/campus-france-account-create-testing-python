
from dataclasses import dataclass

@dataclass
class personne:
    email: str
    motDePasse: str
    confirmationMotDePasse: str
    nom: str
    prenom: str
    paysDeNationalite: str
    codePostal: str
    ville: str
    telephone: str