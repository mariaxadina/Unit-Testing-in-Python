import unittest
from credit_validator import CreditValidator

class TestCreditValidator(unittest.TestCase):
    def setUp(self):
        self.validator = CreditValidator()

    # --- TESTE BLACK-BOX (ECP & BVA) ---
    def test_varsta_limita_inferioara(self):
        # Testam 17 (respins), 18 (admis la varsta)
        self.assertEqual(self.validator.evalueaza_eligibilitate(17, 3000, 600), "Respins: Varsta neadecvata")
        self.assertIn("Aprobat", self.validator.evalueaza_eligibilitate(18, 3000, 600))

    # --- TESTE WHITE-BOX (Coverage) ---
    def test_conditii_excelente(self):
        # Acopera ramura scor_credit > 800
        res = self.validator.evalueaza_eligibilitate(30, 5000, 850)
        self.assertEqual(res, "Aprobat: Conditii Excelente")

    def test_venit_insuficient(self):
        # Testeaza conditia compusa (venit < 2000)
        res = self.validator.evalueaza_eligibilitate(30, 1500, 700)
        self.assertEqual(res, "Respins: Scor sau venit insuficient")