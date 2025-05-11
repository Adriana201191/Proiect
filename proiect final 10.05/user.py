
class Utilizator:
    def __init__(self):
        self.nume = None
        self.email = None

    def valideaza_email(self, email):
        return email and email.endswith(".com") and "@" in email

    def valideaza_parola(self, parola):
        return (
            len(parola) >= 5 and any(c.isupper() for c in parola) and any(c.isdigit() for c in parola)
        )