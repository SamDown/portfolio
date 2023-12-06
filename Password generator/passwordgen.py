import random
import string

def generer_mot_de_passe(longueur):
    lettres = string.ascii_letters
    chiffres = string.digits
    symboles = string.punctuation

    tous_caracteres = lettres + chiffres + symboles

    return ''.join(random.choice(tous_caracteres) for _ in range(longueur))

# Définir la longueur souhaitée pour le mot de passe
longueur_mot_de_passe = 10

# Générer et afficher le mot de passe
print("Your generated password is : ", generer_mot_de_passe(longueur_mot_de_passe))
