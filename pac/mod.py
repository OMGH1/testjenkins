from datetime import datetime


class Voiture:

    def __init__(self, marque, couleur, km=0):
        self.marque = marque
        self.couleur = couleur
        self.annee = datetime.today().year
        self.etat = False
        self.km = km

    def demarrer(self):
        if self.etat:
            print('warning elle est deja demarer')
        else:
            print('demarage ...')
            self.etat = True

    def arreter(self):
        if not self.etat:
            print('warning elle est deja eteinte')
        else:
            print('arret ...')
            self.etat = False

    def rouler(self):
        if not self.etat:
            print('demarer la voiture !')
        else:
            print('vroum')
            self.km += 10


class Humain:

    def __init__(self, nom, age, voiture=None, garage=None):
        self.nom = nom
        self.age = age
        self.voiture = voiture
        self.garage = garage

    def acquerir_voiture(self, new_voiture):
        self.voiture = new_voiture

    def demarer_voiture(self):
        if self.voiture:
            self.voiture.demarer()
        else:
            print('vous ne possedez pas de vehicule')

    def arreter_voiture(self):
        if self.voiture:
            self.voiture.arreter()
        else:
            print('vous ne possedez pas de vehicule')

    def acquerir_garage(self, garage):
        garage.proprietaire = self.nom
        self.garage = garage
        print(f"{self.nom} possede un nouveau garage")

    def deposer_garage(self):
        if not self.voiture:
            print("nous ne possedez pas de voiture")
            raise PasDeVoitureError

        elif not self.garage:
            print("nous ne possedez pas de garage")
            raise PasDeGarageError
        else:
            self.garage.ajout_vehicule(self.voiture)
            self.voiture = None


class Garage:
    pass


class Error(Exception):
    """Base class for other exceptions"""
    pass


class PasDeGarageError(Error):
    """Erreur l'humain ne possede pas de garage"""
    pass


class PasDeVoitureError(Error):
    """Erreur l'humain ne possede pas de voiture"""
    pass


class FizzBuzz:

    def __init__(self,val= 0):
        self.val = val


    # def process_value(self,i):
    #     return i

    # def process_value(self,i):
    #     if i % 3==0:
    #         val = "fizz"
    #     return val

    # def process_value(self,i):
    #     if i % 3==0:
    #         val = "fizz"
    #     elif i % 5 == 0:
    #         val == "buzz"
    #     return val

    # def process_value(self,i):
    #     if i % 15 == 0:
    #         val = "fizzbuzz"
    #     elif i % 3 == 0:
    #         val = "fizz"
    #     elif i % 5 == 0:
    #         val = "buzz"
    #     return val

    def convert_values(self, i):
        if i % 15 == 0:
            val = "fizzbuzz"
        elif i % 3 == 0:
            val = "fizz"
        elif i % 5 == 0:
            val = "buzz"
        else :
            val = str(i)
        return val

    #def process_values(self):
    #    return "".join([self.convert_values(x)  for x in self.val])

    def process_values(self):
        if isinstance(self.val, int):
            self.convert_values(int)
        if isinstance(self.val, list):
            return "".join([self.convert_values(x) for x in self.val])


if __name__ == '__main__':
    pass 
