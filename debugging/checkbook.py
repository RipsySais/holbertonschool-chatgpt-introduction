#!/bin/python3
class Checkbook:
    def __init__(self):
        """
        Initialise une nouvelle instance de Checkbook avec un solde de 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Dépose un montant spécifié sur le compte.

        Arguments :
        amount (float) : Le montant à déposer.
        """
        self.balance += amount
        print(f"Déposé ${amount:.2f}")
        print(f"Solde actuel : ${self.balance:.2f}")

    def withdraw(self, amount):
        """
        Retire un montant spécifié du compte si le solde est suffisant.

        Arguments :
        amount (float) : Le montant à retirer.
        """
        if amount > self.balance:
            print("Fonds insuffisants pour effectuer le retrait.")
        else:
            self.balance -= amount
            print(f"Retiré ${amount:.2f}")
            print(f"Solde actuel : ${self.balance:.2f}")

    def get_balance(self):
        """
        Affiche le solde actuel du compte.
        """
        print(f"Solde actuel : ${self.balance:.2f}")

def main():
    cb = Checkbook()
    while True:
        action = input("Que souhaitez-vous faire ? (deposit, retrait, solde, sortie) : ").lower()
        if action == 'sortie':
            break
        elif action == 'deposit':

                amount = float(input("Entrez le montant à déposer : $"))
                cb.deposit(amount)


        elif action == 'retrait':

                amount = float(input("Entrez le montant à retirer : $"))
                cb.withdraw(amount)

        elif action == 'solde':
            cb.get_balance()
        else:
            print("Commande non valide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
