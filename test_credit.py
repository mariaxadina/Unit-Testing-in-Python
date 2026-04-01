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

    # --- TESTE PENTRU VENIT LUNAR (BVA & ECP) ---
    def test_venit_exact_limita(self):
        # Frontiera: 2000 este venitul minim acceptat
        res = self.validator.evalueaza_eligibilitate(30, 2000, 600)
        self.assertIn("Aprobat", res)

    def test_venit_sub_limita(self):
        # Frontiera: 1999 ar trebui sa fie respins
        res = self.validator.evalueaza_eligibilitate(30, 1999, 600)
        self.assertEqual(res, "Respins: Scor sau venit insuficient")

    # --- TESTE PENTRU SCOR CREDIT (Decision & Condition Coverage) ---
    def test_scor_la_limita_de_respingere(self):
        # Frontiera: 500 este respins (conditia in cod este scor > 500)
        res = self.validator.evalueaza_eligibilitate(30, 3000, 500)
        self.assertEqual(res, "Respins: Scor sau venit insuficient")
