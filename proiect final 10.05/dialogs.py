from PySide6.QtCore import Signal, Qt
from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QTextEdit, QPushButton, QMessageBox, QLineEdit, QFormLayout, \
    QHBoxLayout, QWidget, QMainWindow, QComboBox
from skincare import SkincareRecomandari
from user import Utilizator
from auth import Autentificare


class RegisterDialog(QDialog):
    registration_success = Signal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Register")
        self.setFixedSize(400, 250)
        self.utilizator = Utilizator()
        self.autentificare = Autentificare()
        self.setStyleSheet("""
                    QDialog {
                        background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ebcbf5,stop: 1 #ffffff);
                    }
                    QLabel {
                        color: black;
                        font-family: "Calibri";
                        font-weight: bold;
                        font-size: 16px;
                    }
                    QLineEdit {
                        background-color: #F2F2F2;
                        color: black;
                        font-family: "Calibri";
                        font-size: 12px;
                        font-weight: bold;
                        padding: 6px;
                    }
                    QPushButton {
                        background-color: #ebcbf5;   
                        color: black;
                        font-size: 16px;
                        font-weight: bold;
                        padding: 14px;
                        font-family: Calibri;
                    }
                """)
        self.init_ui()


    def init_ui(self):
        layout = QFormLayout()

        self.nume_input = QLineEdit()
        layout.addRow("Nume utilizator:", self.nume_input)

        self.email_input = QLineEdit()
        layout.addRow("Email:", self.email_input)

        self.parola_input = QLineEdit()
        self.parola_input.setEchoMode(QLineEdit.Password)
        layout.addRow("Parolă:", self.parola_input)

        self.submit_button = QPushButton("Register")
        self.submit_button.clicked.connect(self.creare_utilizator)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def creare_utilizator(self):
        nume = self.nume_input.text()
        email = self.email_input.text()
        parola = self.parola_input.text()

        if not nume:
            QMessageBox.warning(self, "Eroare", "Numele de utilizator nu poate fi gol!")
            return

        if not self.utilizator.valideaza_email(email):
            QMessageBox.warning(self, "Eroare", "Adresa de email este invalidă!")
            return

        if not self.utilizator.valideaza_parola(parola):
            QMessageBox.warning(self, "Eroare", "Parola este invalidă!\nParola trebuie sa contina minim 5 caractere, cel putin o litera mare si cel putin o cifra.")
            return

        if nume in self.autentificare.baza_date:
            QMessageBox.warning(self, "Eroare", "Acest nume de utilizator există deja!")
            return

            # Verifică dacă emailul există deja
        for user, data in self.autentificare.baza_date.items():
            if data["email"] == email:
                QMessageBox.warning(self, "Eroare", "Exista deja un cont creat cu aceasta adresa de mail!")
                return


        if self.autentificare.register(nume, email, parola):
            QMessageBox.information(self, "Succes", "Utilizator creat cu succes!")
            self.registration_success.emit()
            self.accept()
        else:
            QMessageBox.warning(self, "Eroare",
                                "Înregistrare eșuată!")  # Ar trebui să fie rare cazurile când ajunge aici

class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setFixedSize(400, 250)
        self.autentificare = Autentificare()
        self.setStyleSheet("""
                   QDialog {
                       background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ebcbf5,stop: 1 #ffffff);
                   }
                   QLabel {
                       color: black;
                       font-family: "Calibri";
                       font-weight: bold;
                       font-size: 16px;
                   }
                   QLineEdit {
                       background-color: #F2F2F2;
                       color: black;
                       font-family: "Calibri";
                       font-size: 12px;
                       font-weight: bold;
                       padding: 6px;
                   }
                   QPushButton {
                       background-color: #ebcbf5;   
                        color: black;
                        font-size: 16px;
                        font-weight: bold;
                        padding: 14px;
                        font-family: Calibri;
                   }
               """)
        self.init_ui()

    def init_ui(self):
        layout = QFormLayout()

        self.username_input = QLineEdit()
        layout.addRow("Nume utilizator:", self.username_input)

        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addRow("Parolă:", self.password_input)

        self.submit_button = QPushButton("Login")
        self.submit_button.clicked.connect(self.login)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def login(self):
        username = self.username_input.text()
        parola = self.password_input.text()

        if self.autentificare.login(username, parola):
            QMessageBox.information(self, "Succes", "Autentificare reușită!")
            self.accept()
        else:
            QMessageBox.warning(self, "Eroare", "Nume de utilizator sau parolă greșită!")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Skincare App")
        self.setFixedSize(600, 600)
        self.recomandari = SkincareRecomandari()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        title_label = QLabel("Bine ai venit!\n\n\nArta îngrijirii pielii\nîncepe cu tine!")  #Self care \nstarts with \nskin care!
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("color: #470961; background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ebcbf5, "
                                  "stop: 1 #ffffff) ;font-size: 62px; font-weight: bold;font-family: FreeStyle Script")
        layout.addWidget(title_label)


        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.open_login)
        self.login_button.setStyleSheet("""
            QPushButton {
                background-color: #ebcbf5;   
                color: black;
                font-size: 16px;
                font-weight: bold;
                padding: 14px;
                font-family: Calibri;
            }
        """)
        layout.addWidget(self.login_button)

        self.register_button = QPushButton("Register")
        self.register_button.clicked.connect(self.open_register)
        self.register_button.setStyleSheet("""
            QPushButton {
                background-color: #ebcbf5;   
                color: black;
                font-size: 16px;
                font-weight: bold;
                padding: 14px;
                font-family: Calibri;
            }
        """)
        layout.addWidget(self.register_button)

        self.container = QWidget()
        self.container.setLayout(layout)
        self.setCentralWidget(self.container)

    def open_login(self):
        dialog = LoginDialog()
        if dialog.exec():
            self.open_skincare()

    def open_register(self):
        dialog = RegisterDialog()
        dialog.registration_success.connect(self.open_skincare)
        dialog.exec()

    def open_skincare(self):

        self.hide()
        self.skincare_window = SkincareWindow(self.recomandari, self)
        self.skincare_window.show()


class SkincareWindow(QMainWindow):
    def __init__(self, recomandari, main_window):
        super().__init__()
        self.main_window = main_window
        self.recomandari = recomandari
        self.setWindowTitle("Recomandări Skincare")
        self.setFixedSize(400, 200)
        self.setStyleSheet("""
                    QDialog {
                        background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ebcbf5,stop: 1 #ffffff);
                    }
                    QLabel {
                        color: black;
                        font-family: "Calibri";
                        font-weight: bold;
                        font-size: 16px;
                    }
                    QLineEdit {
                        background-color: #F2F2F2;
                        color: black;
                        font-family: "Calibri";
                        font-size: 12px;
                        font-weight: bold;
                        padding: 6px;
                    }
                    QPushButton {
                        background-color: #ebcbf5;   
                        color: black;
                        font-size: 16px;
                        font-weight: bold;
                        padding: 14px;
                        font-family: Calibri;
                    }
                """)
        self.setStyleSheet(self.styleSheet() + """
                    QComboBox {
                        background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ebcbf5,stop: 1 #ffffff);
                        color: black;
                        font-family: "Calibri";
                        font-size: 14px;
                        padding: 6px;
                        border: 1px solid #cccccc;
                        border-radius: 4px;
                    }
                    QComboBox::drop-down {
                        border: none;
                        }
                    QComboBox QAbstractItemView {
                        background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ebcbf5,stop: 1 #ffffff);
                    }
                """)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.skin_type_label = QLabel("Selectează tipul pielii tale:")
        layout.addWidget(self.skin_type_label)

        self.skin_type_combo = QComboBox()
        self.skin_type_combo.addItems(self.recomandari.recomandari.keys())
        layout.addWidget(self.skin_type_combo)

        self.recommendations_button = QPushButton("Afișează recomandările")

        self.recommendations_button.clicked.connect(self.show_recommendations)
        layout.addWidget(self.recommendations_button)

        self.container = QWidget()
        self.container.setLayout(layout)
        self.setCentralWidget(self.container)

    def show_recommendations(self):
        tip_piele = self.skin_type_combo.currentText()
        recomandari = self.recomandari.afiseaza_recomandari(tip_piele)


        if recomandari:
            dialog = RecomandariDialog(tip_piele, recomandari, self)
            dialog.exec()
            self.open_submenu(tip_piele)
        else:
            QMessageBox.warning(self, "Eroare", "Nu există recomandări pentru acest tip de piele.")

    def open_submenu(self, tip_piele):
        submenu = SubMenuDialog(tip_piele, self, self.main_window, self.recomandari)
        submenu.exec()

class RecomandariDialog(QDialog):
    def __init__(self, tip_piele, recomandari, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Recomandări")
        self.setFixedSize(800, 400)
        self.setStyleSheet("background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ebcbf5, stop: 1 #ffffff);")
        layout = QVBoxLayout()

        mesaj = f"Recomandări pentru pielea {tip_piele}:\n"
        mesaj += "\nDimineața:\n" + "\n".join(recomandari["Dimineața"])
        mesaj += "\n\nSeara:\n" + "\n".join(recomandari["Seara"])

        self.text_edit = QTextEdit()
        self.text_edit.setText(mesaj)
        self.text_edit.setReadOnly(True)

        self.text_edit.setStyleSheet("color: black; font-family: Calibri; font-weight: bold;font-size: 16px")

        layout.addWidget(self.text_edit)

        button_inchide = QPushButton("Închide")
        button_inchide.clicked.connect(self.accept)
        layout.addWidget(button_inchide)

        self.setLayout(layout)



class SubMenuDialog(QDialog):
    def __init__(self, tip_piele, skincare_window, main_window, recomandari, parent=None):
        super().__init__(parent)
        self.tip_piele = tip_piele
        self.skincare_window = skincare_window
        self.main_window = main_window
        self.recomandari = recomandari
        self.setWindowTitle("Submeniu")
        self.setFixedSize(400, 300)
        self.setStyleSheet("""
                            QDialog {
                                background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ebcbf5,stop: 1 #ffffff);
                            }
                            QLabel {
                                color: black;
                                font-family: "Calibri";
                                font-weight: bold;
                                font-size: 16px;
                            }
                            QLineEdit {
                                background-color: #F2F2F2;
                                color: black;
                                font-family: "Calibri";
                                font-size: 12px;
                                font-weight: bold;
                                padding: 6px;
                            }
                            QPushButton {
                                background-color: #ebcbf5;   
                                color: black;
                                font-size: 16px;
                                font-weight: bold;
                                padding: 14px;
                                font-family: Calibri;
                            }
                        """)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        label = QLabel("Alegeți o opțiune:")
        layout.addWidget(label)

        btn_produse = QPushButton("Recomandări Produse")
        btn_produse.clicked.connect(self.show_product_recommendations)
        layout.addWidget(btn_produse)

        btn_meniu = QPushButton("Meniu Principal")
        btn_meniu.clicked.connect(self.goto_main_menu)
        layout.addWidget(btn_meniu)

        btn_logout = QPushButton("LogOut")
        btn_logout.clicked.connect(self.logout)
        layout.addWidget(btn_logout)

        self.setLayout(layout)

    def show_product_recommendations(self):
        prod_dialog = ProductsDialog(self.recomandari, self.tip_piele, self)
        prod_dialog.exec()

    def goto_main_menu(self):

        self.accept()

    def logout(self):
        self.accept()
        self.skincare_window.close()
        self.main_window.show()


class ProductsDialog(QDialog):
    def __init__(self, recomandari, tip_piele, parent=None):
        super().__init__(parent)
        self.recomandari = recomandari
        self.tip_piele = tip_piele
        self.setWindowTitle("Recomandări Produse")
        self.setFixedSize(800, 400)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()


        links_dict = self.recomandari.produse_recomandate(self.tip_piele)


        header_dimineata = QLabel("Dimineața:")
        header_dimineata.setStyleSheet("font-weight: bold; font-size: 16px;")
        layout.addWidget(header_dimineata)


        dimineata_links = links_dict.get("Dimineața", [])
        for link in dimineata_links:
            lbl = QLabel(f"<a href='{link}'>{link}</a>")
            lbl.setOpenExternalLinks(True)
            layout.addWidget(lbl)

        layout.addSpacing(20)


        header_seara = QLabel("Seara:")
        header_seara.setStyleSheet("font-weight: bold; font-size: 16px;")
        layout.addWidget(header_seara)


        seara_links = links_dict.get("Seara", [])
        for link in seara_links:
            lbl = QLabel(f"<a href='{link}'>{link}</a>")
            lbl.setOpenExternalLinks(True)
            layout.addWidget(lbl)

        self.setLayout(layout)