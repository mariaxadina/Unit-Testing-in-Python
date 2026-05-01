from credit_validator import CreditValidator

validator = CreditValidator()

teste = [
    ("20", 3000, 600),
    (20, "3000", 600),
    (17, 3000, 600),
    (18, 3000, 600),
    (65, 3000, 600),
    (66, 3000, 600),
    (30, 1999, 700),
    (30, 3000, 500),
    (30, 1500, 900),
    (30, 2000, 501),
    (30, 3000, 800),
    (40, 4000, 700),
    (30, 3000, 801),
    (50, 7000, 900),
]

for i, (v, venit, scor) in enumerate(teste, start=1):
    try:
        rezultat = validator.evalueaza_eligibilitate(v, venit, scor)
    except Exception as e:
        rezultat = type(e).__name__

    print(f"Test {i}: Input=({v}, {venit}, {scor}) -> Output={rezultat}")