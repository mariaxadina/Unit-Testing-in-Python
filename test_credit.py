import unittest
from credit_validator import CreditValidator

class TestCreditValidator(unittest.TestCase):

    def setUp(self):
        self.validator = CreditValidator()

    # type check - circuit 1
    def test_date_invalide_varsta_string(self):
        with self.assertRaises(TypeError):
            self.validator.evalueaza_eligibilitate("20", 3000, 600)

    def test_date_invalide_venit_string(self):
        with self.assertRaises(TypeError):
            self.validator.evalueaza_eligibilitate(20, "3000", 600)


    # varsta - circuit 2
    def test_varsta_sub_limita(self):
        self.assertEqual(
            self.validator.evalueaza_eligibilitate(17, 3000, 600),
            "Respins: Varsta neadecvata"
        )

    def test_varsta_limita_inferioara(self):
        self.assertIn(
            "Aprobat",
            self.validator.evalueaza_eligibilitate(18, 3000, 600)
        )

    def test_varsta_limita_superioara(self):
        self.assertIn(
            "Aprobat",
            self.validator.evalueaza_eligibilitate(65, 3000, 600)
        )

    def test_varsta_peste_limita(self):
        self.assertEqual(
            self.validator.evalueaza_eligibilitate(66, 3000, 600),
            "Respins: Varsta neadecvata"
        )


    # venit + scor respins - circuit 3
    def test_venit_sub_limita(self):
        self.assertEqual(
            self.validator.evalueaza_eligibilitate(30, 1999, 700),
            "Respins: Scor sau venit insuficient"
        )

    def test_scor_sub_limita(self):
        self.assertEqual(
            self.validator.evalueaza_eligibilitate(30, 3000, 500),
            "Respins: Scor sau venit insuficient"
        )

    def test_scor_bun_dar_venit_mic(self):
        self.assertEqual(
            self.validator.evalueaza_eligibilitate(30, 1500, 900),
            "Respins: Scor sau venit insuficient"
        )


    # aprobat standard - circuit 4
    def test_scor_minim_aprobare(self):
        self.assertEqual(
            self.validator.evalueaza_eligibilitate(30, 2000, 501),
            "Aprobat: Conditii Standard"
        )

    def test_scor_800_standard(self):
        self.assertEqual(
            self.validator.evalueaza_eligibilitate(30, 3000, 800),
            "Aprobat: Conditii Standard"
        )

    def test_caz_standard_general(self):
        self.assertEqual(
            self.validator.evalueaza_eligibilitate(40, 4000, 700),
            "Aprobat: Conditii Standard"
        )


    # aprobat excelent - circuit 5
    def test_scor_excelent_minim(self):
        self.assertEqual(
            self.validator.evalueaza_eligibilitate(30, 3000, 801),
            "Aprobat: Conditii Excelente"
        )

    def test_scor_excelent_mare(self):
        self.assertEqual(
            self.validator.evalueaza_eligibilitate(50, 7000, 900),
            "Aprobat: Conditii Excelente"
        )

   #Teste input de tip invalid sau inexistent
   # BOBO - Testare pentru tipuri de date și parametri absenți
    
    def test_varsta_none(self):
        with self.assertRaises(TypeError):
            self.validator.evalueaza_eligibilitate(None, 3000, 600)

    def test_parametri_insuficienti(self):
        with self.assertRaises(TypeError):
            # Lipsește al treilea parametru (scor_credit)
            self.validator.evalueaza_eligibilitate(30, 3000)

    def test_tip_data_invalid_lista(self):
        with self.assertRaises(TypeError):
            self.validator.evalueaza_eligibilitate(30, [2000], 600)

    def test_scor_credit_string(self):
        with self.assertRaises(TypeError):
            self.validator.evalueaza_eligibilitate(30, 3000, "700")


if __name__ == "__main__":
    unittest.main()