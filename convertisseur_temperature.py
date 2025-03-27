# un convertisseur de température

def convertisseur_temperature():
    """Fonction qui permet de convertir les températures:'C' pour Celsius, 'F' pour Fahrenheit et 'K' pour Kelvin
    """""
    try:
        valeur=float(input("quelle est la valeur à convertir?"))
        unite_initiale=input("quelle est l'unité initiale?'C' pour Celsius, 'F' pour Fahrenheit et 'K' pour Kelvin ")
        unite_finale=input("Vers quelle unité voulez vous faire la convertion? 'C' pour Celsius, 'F' pour Fahrenheit et 'K' pour Kelvin")
        
        # Les conditions d'erreur d'unité 
        if unite_initiale not in ("C", "F", "K","c","f","k") or unite_finale not in ("C", "F", "K","c","f","k"):
                raise ValueError("Unités invalides. Utilisez 'C', 'F' ou 'K'.")
        
        # Les conditions pour le degre celsius
        if unite_initiale.upper()=="K" and unite_finale.upper()=="C":
            resultat=valeur-273.15
            
        elif unite_initiale.upper()=="F" and unite_finale.upper()=="C":
            resultat=(valeur-32)*5/9
            
        elif unite_initiale.upper()=="C" and unite_finale.upper()=="C":
            resultat=valeur
        
        # Les conditions pour le degre Fahrenheit
        if unite_initiale.upper()=="K" and unite_finale.upper()=="F":
            resultat=valeur*9/5-459.67
            
        elif unite_initiale.upper()=="C" and unite_finale.upper()=="F":
            resultat=(valeur*9/5)+32
            
        elif unite_initiale.upper()=="F" and unite_finale.upper()=="F":
            resultat=valeur
        
        # Les conditions pour le degre kelvin
        if unite_initiale.upper()=="C" and unite_finale.upper()=="K":
            resultat=valeur+273.15
            
        elif unite_initiale.upper()=="F" and unite_finale.upper()=="K":
            resultat=(valeur+459.67)*5/9
            
        elif unite_initiale.upper()=="K" and unite_finale.upper()=="K":
            resultat=valeur
        print(f"{valeur}°{unite_initiale.upper()}={resultat:.2F}°{unite_finale.upper()}")

    # Gestion des erreurs générales   
    except ValueError as e:
        print(f"Erreur: {e}")
    except Exception as e:
        print(f"Une erreur inattendue s'est produite: {e}")
    
convertisseur_temperature()
