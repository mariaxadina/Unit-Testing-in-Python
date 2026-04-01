import unittest
from credit_validator import CreditValidator

class TestCreditValidator(unittest.TestCase):
    def setUp(self):
        self.validator = CreditValidator()

    
    def test_varsta_limita_inferioara(self):
        self.assertEqual(self.validator.evalueaza_eligibilitate(17, 3000, 600), "Respins: Varsta neadecvata")
        self.assertIn("Aprobat", self.validator.evalueaza_eligibilitate(18, 3000, 600))

   
    def test_conditii_excelente(self):
        res = self.validator.evalueaza_eligibilitate(30, 5000, 850)
        self.assertEqual(res, "Aprobat: Conditii Excelente")

    def test_venit_insuficient(self):
        res = self.validator.evalueaza_eligibilitate(30, 1500, 700)
        self.assertEqual(res, "Respins: Scor sau venit insuficient")


    def test_venit_exact_limita(self):
        res = self.validator.evalueaza_eligibilitate(30, 2000, 600)
        self.assertIn("Aprobat", res)

    def test_venit_sub_limita(self):
        res = self.validator.evalueaza_eligibilitate(30, 1999, 600)
        self.assertEqual(res, "Respins: Scor sau venit insuficient")

    
    def test_scor_la_limita_de_respingere(self):
        #500 este respins (conditia in cod este scor > 500)
        res = self.validator.evalueaza_eligibilitate(30, 3000, 500)
        self.assertEqual(res, "Respins: Scor sau venit insuficient")
