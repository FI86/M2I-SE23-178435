# Exercice 17
# Écrivez un script qui calcule combien de jours avant le prochain poisson d'avril ?
from datetime import date

def main():
    aujourdhui = date.today()
    avril = date(aujourdhui.year, 4, 1)

    if avril < aujourdhui: avril = date(aujourdhui.year + 1, 4, 1)

    print(f"Date du prochain poisson d'avril : {avril.day:>02d}/{avril.month:>02d}/{avril.year}")
    print(f"Nombre de jours avant le prochaine poisson d'avril : {(avril - aujourdhui).days}")

    print("_" * 40)
    input("Appuyer sur <Entrée> pour terminer !")

if __name__ == "__main__":
    main()
