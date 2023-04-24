import sys
import pac
from pac.mod import Voiture, Humain, Garage, PasDeGarageError, PasDeVoitureError, FizzBuzz
import unittest
from unittest.mock import Mock


#  le setup, et les skips

class Testvoiture(unittest.TestCase):

    def setUp(self):
        self.voiture_off = Voiture('Rennault', 'rouge')
        self.voiture_on = Voiture('Rennault', 'rouge')
        self.voiture_on.demarrer()

    # Test creation d'une l'instance voiture
    def test_init(self):
        self.assertIsInstance(self.voiture_off, Voiture)

    # Test demarrer une instance de voiture
    def test_demarrer(self):
        self.voiture_off.demarrer()
        self.assertTrue(self.voiture_off.etat)

    # Test Arreter une instance de voiture en etat "True"
    def test_arreter(self):
        self.voiture_on.arreter()
        self.assertFalse(self.voiture_on.etat)

    # Test rouler avec un vehicule en etat "True"
    def test_rouler(self):
        self.voiture_on.rouler()
        self.assertEqual(self.voiture_on.km, 10)

    # skip en fonction de l environement
    @unittest.skipUnless(sys.platform.startswith("win"), "Windows requis pour ce test")
    def test_os(self):
        print('windows ....')

    @unittest.skipIf(pac.__version__ > 1, "fonctionnalité non incluse dans la présente version")
    def test_voiture_electrique(self):
        print('version ....')

# Humain test, mock

class TestHumain(unittest.TestCase):


    def setUp(self):
        # humain
        self.humain = Humain("Damien",38)

        # humain + voiture
        self.automobiliste1 = Humain("Pierre", 28)
        self.voiture_off = Voiture('Rennault', 'rouge')
        self.automobiliste1.voiture =self.voiture_off

        # humain + voiture + garage
        self.automobiliste2 = Humain("Pierre", 28)
        self.automobiliste2.voiture = self.voiture_off
        self.mock_garage = Mock(spec=Garage)
        self.mock_garage.ajout_vehicule = Mock(return_value="None")
        self.automobiliste2.garage = self.mock_garage

    def test_acquerir_voiture(self):
        self.humain.acquerir_voiture(self.voiture_off)
        self.assertIsInstance(self.humain.voiture, Voiture)

    def test_deposer_gararge(self):
        self.automobiliste2.deposer_garage()
        self.assertIsNone(self.automobiliste2.voiture)

    def test_acquerir_garage(self):
        self.automobiliste1.acquerir_garage(self.mock_garage)
        self.assertIsInstance(self.automobiliste1.garage, Garage)
        self.assertEqual(self.automobiliste1.garage.proprietaire,"Pierre")

    def test_Errors(self):
        with self.assertRaises(PasDeVoitureError):
            self.humain.deposer_garage()

        with self.assertRaises(PasDeGarageError):
            self.automobiliste1.deposer_garage()

        with self.assertRaises(AttributeError):
            self.automobiliste2.deposer_garage()
            self.automobiliste2.voiture.demarrer()


class TestFizzBuzz(unittest.TestCase):
    def setUp(self):
        self.fizz = FizzBuzz()



    def test_by3(self):
        """
        Tester les multiple de 3.
        """
        liste = [3, 6, 9]
        for i in liste:
            with self.subTest(i=i):
                self.assertEqual(self.fizz.convert_values(i), "fizz")

    def test_by5(self):
        """
        Tester les multiple de 5.
        """
        liste = [5, 10, 20]
        for i in liste:
            with self.subTest(i=i):
                self.assertEqual(self.fizz.convert_values(i), "buzz")

    def test_by15(self):
        """
        Tester les multiple de 15.
        """
        liste = [15, 30, 45]
        for i in liste:
            with self.subTest(i=i):
                self.assertEqual(self.fizz.convert_values(i), "fizzbuzz")

    def test_byx(self):
        """
        Tester quelque chiffres
        """
        liste = [2, 8, 13]
        for i in liste:
            with self.subTest(i=i):
                self.assertEqual(self.fizz.convert_values(i), str(i))
    def test_bylist(self):
        """
        Tester la liste [3, 4, 5, 7, 15].
        """
        liste = [3, 4, 5, 7, 15]
        self.fizz = FizzBuzz(liste)
        self.assertEqual(self.fizz.process_values(), "fizz4buzz7fizzbuzz")


if __name__ == '__main__':
    unittest.main()
