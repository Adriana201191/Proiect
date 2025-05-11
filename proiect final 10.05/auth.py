import json
from user import Utilizator


class Autentificare:
    def __init__(self):
        self.baza_date = self.load_database()

    @staticmethod
    def load_database():
        try:
            with open('baza_date.json', 'r') as file:
                data = json.load(file)
                return data["users"]
        except FileNotFoundError:
            print("Fișierul baza_date.json nu a fost găsit. Va fi creat la prima înregistrare.")
            return {}
        except json.JSONDecodeError:
            print("Eroare la decodificarea JSON. Asigură-te că fișierul JSON este valid.")
            return {}
        except Exception as e:
            print(f"Eroare la încărcarea bazei de date: {e}")
            return {}

    def login(self, username, parola):
        user_data = self.baza_date.get(username)
        if user_data:
            return user_data["parola"] == parola
        return False

    def register(self, username, email, parola):
        if username in self.baza_date:
            return False

        self.baza_date[username] = {"email": email, "parola": parola}
        self.save_database()
        return True

    def save_database(self):
        try:
            with open('baza_date.json', 'w') as file:
                json.dump({"users": self.baza_date}, file, indent=4)
        except Exception as e:
            print(f"Eroare la salvarea bazei de date: {e}")