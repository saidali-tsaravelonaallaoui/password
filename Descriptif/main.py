import random
import hashlib

def is_valid_pass(password):
    return (
        len(password) >= 8
        and any(c.isupper() for c in password)
        and any(c.islower() for c in password)
        and any(c.isdigit() for c in password)
        and any(c in "!@#$%^&*" for c in password)
    )

def verif_pass():
    return input("Veuillez entrer votre mot de passe : ")

def main():
    try:
        while True:
            password = verif_pass()
            if is_valid_pass(password):
                pass_hash = hashlib.sha256(password.encode()).hexdigest()

                print("Mot de passe valide. \nMot de passe haché avec SHA-256 :", pass_hash)
                break
            else:
                print("Mot de passe invalide. Veuillez respecter les exigences de sécurité.")
                
    except KeyboardInterrupt:
        print('\nArret du programme')
        import sys
        sys.exit(0)

if __name__ == "__main__":
    main()