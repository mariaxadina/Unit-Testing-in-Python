class CreditValidator:
    def evalueaza_eligibilitate(self, varsta, venit_lunar, scor_credit):
        """
        Determina daca un client este eligibil pentru un credit.
        Reguli:
        1. Varsta intre 18 si 65 ani (inclusiv).
        2. Venit minim 2000 RON.
        3. Scorul de credit trebuie sa fie peste 500.
        """
        if not (isinstance(varsta, int) and isinstance(venit_lunar, (int, float))):
            raise TypeError("Datele de intrare trebuie sa fie numerice")

        # Verificare limite varsta (ECP & BVA)
        if varsta < 18 or varsta > 65:
            return "Respins: Varsta neadecvata"

        # Verificare conditii financiare (Decision & Condition Coverage)
        if venit_lunar >= 2000 and scor_credit > 500:
            if scor_credit > 800:
                return "Aprobat: Conditii Excelente"
            return "Aprobat: Conditii Standard"
        else:
            return "Respins: Scor sau venit insuficient"