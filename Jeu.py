import random

def guess_the_number():
    # Générer un nombre aléatoire entre 1 et 10
    secret_number = random.randint(1, 10)
    
    print("Bienvenue dans le jeu Guess the Number!")
    print("Devinez le nombre entre 0 et 10.")

    while True:
        # Demander à l'utilisateur de deviner le nombre
        user_guess = int(input("Entrez votre guess : "))

        # Vérifier si le guess est correct
        if user_guess == secret_number:
            print("Félicitations ! Tu as deviné le bon nombre.")
            break
        else:
            print("Désolé, ce n'est pas le bon nombre. Essayez à nouveau.")

if __name__ == "__main__":
    guess_the_number()
