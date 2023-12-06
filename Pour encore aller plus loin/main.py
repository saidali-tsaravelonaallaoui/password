import random
import hashlib
import json
import string

def is_valid_password(password):
    return (
        len(password) >= 8
        and any(c.isupper() for c in password)
        and any(c.islower() for c in password)
        and any(c.isdigit() for c in password)
        and any(c in "!@#$%^&*" for c in password)
    )

def get_user_password():
    return input("Veuillez entrer votre mot de passe : ")

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def save_passwords(passwords):
    with open("passwords.json", "w") as file:
        json.dump(passwords, file)

def load_passwords():
    try:
        with open("passwords.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def display_passwords(passwords):
    if passwords:
        print("Mots de passe enregistrés :")
        for password in passwords:
            print(password)
    else:
        print("Aucun mot de passe enregistré.")

def compare_passwords(passwords, hashed_password):
    return hashed_password in passwords

def generate_random_password():
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choice(characters) for _ in range(12))
    return password

def main():
    passwords = load_passwords()
    try:
        while True:
            print("\n1. Ajouter un nouveau mot de passe")
            print("2. Afficher les mots de passe")
            print("3. Générer un mot de passe aléatoire")
            print("4. Quitter")

            choice = input("Choisissez une option (1/2/3/4) : ")

            if choice == "1":
                password = get_user_password()

                if is_valid_password(password):
                    hashed_password = hash_password(password)

                    if not compare_passwords(passwords, hashed_password):
                        passwords.append(hashed_password)
                        save_passwords(passwords)
                        print("Mot de passe enregistré avec succès.")
                    else:
                        print("Ce mot de passe est déjà enregistré.")
                else:
                    print("Mot de passe invalide. Veuillez respecter les exigences de sécurité.")

            elif choice == "2":
                display_passwords(passwords)

            elif choice == "3":
                random_password = generate_random_password()
                print("Mot de passe aléatoire généré :", random_password)

            elif choice == "4":
                print("Programme terminé.")
                break

            else:
                print("Option invalide. Veuillez choisir une option valide.")
    except KeyboardInterrupt:
                print('\nArret du programme')
                import sys
                sys.exit(0)
            
if __name__ == "__main__":
    main()