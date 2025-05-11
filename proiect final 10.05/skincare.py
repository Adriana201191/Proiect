

class SkincareRecomandari:
    def __init__(self):
        self.recomandari = {
            "Grasă": {
                "Dimineața": [
                    "\n1.Curățare:\nUn gel de curățare non-comedogenic",
                    "2.Tonifiere:\n Un toner cu acid salicilic (sau extracte de plante calmante)",
                    "3.Ser:\n Un ser cu vitamina C/niacinamidă",
                    "4.Hidratare ușoară:\n O cremă hidratantă ușoară, oil-free, cu textură gel sau emulsie",
                    "5.Protecție solară:\n Un produs cu SPF 30/50 cu formulă matifiantă\n\n"
                ],
                "Seara": ["\n1.Curățare în profunzime (Double Cleanse):\nPrimul pas: Un demachiant pe bază de ulei sau o apă micelară\nAl doilea pas: Un gel sau spumă de curățare delicat, similar cu cel utilizat dimineața.",
                          "2.Exfoliere (1-2 ori pe săptămână):\nUn exfoliant chimic cu acid salicilic",
                          "3.Tonifiere:\nUn toner cu ingrediente calmante",
                          "4.Tratament specific:\nUn ser cu ingrediente ce ajută la reglarea producției de sebum (ex. niacinamidă) sau o formulă cu retinol în doze mici",
                          "5.Hidratare de noapte:\nO cremă hidratantă puțin mai bogată decât cea de dimineață",
                          "6.Opțional:\n Mască de Argilă"
                          ]
            },
            "Uscată": {
                "Dimineața": [
                    "\n1.Curățare delicată:\nUn lapte demachiant sau o loțiune de curățare care nu îndepărtează excesul de uleiuri naturale ale pielii",
                    "2.Tonifiere blândă:\nUn toner hidratant, fără alcool, care să calmeze pielea",
                    "3.Ser:\n Un ser cu acid hialuronic sau vitamina E",
                    "4.Hidratare intensă:\n O cremă hidratantă intensa, care să hrănească și să protejeze bariera naturală a pielii",
                    "5.Protecție solară:\n Un produs cu SPF 30/50 cu formulă matifiantă\n\n"
                ],
                "Seara": ["\n1.Curățare în profunzime (Double Cleanse):\nPrimul pas: Un demachiant pe bază de ulei sau o apă micelară\nAl doilea pas: Un gel sau spumă de curățare delicat, similar cu cel utilizat dimineața.",
                          "2.Exfoliere blândă(1-2 ori pe săptămână):\nUn acid exfoliant mai blând (ex. acid lactic)",
                          "3.Tonifiere blândă:\nUn toner hidratant, fără alcool, care să calmeze pielea",
                          "4.Tratament specific:\nUn ser hidratant, eventual combinat cu celule active nutritive (cum ar fi acidul hialuronic sau peptidele)",
                          "5.Hidratare de noapte:\nO cremă de noapte mai bogată decât cea de zi, poți adăuga și câteva picături de ulei facial (precum cel de argan sau jojoba).",
                          "6.Opțional:\n Mască hidratantă"
                          ]
            },
            "Mixtă": {
                "Dimineața": [
                    "\n1.Curățare delicată:\nUn gel sau spumă de curățare non-iritant",
                    "2.Tonifiere/ Balansare pH:\n Un toner cu ingrediente calmante",
                    "3.Ser antioxidant:\n Un ser cu vitamina C sau antioxidanți",
                    "4.Hidratare ușoară:\n O cremă hidratantă lejeră, de tip gel sau emulsie, non-comedogenică",
                    "5.Protecție solară:\n Un produs cu SPF 30/50 cu textură ușoară\n\n"
                ],
                "Seara": ["\n1.Curățare în profunzime (Double Cleanse):\nPrimul pas: Un demachiant pe bază de ulei sau o apă micelară\nAl doilea pas: Un gel sau spumă de curățare delicat, similar cu cel utilizat dimineața.",
                          "2.Tonifiere:\nUn toner cu ingrediente calmante",
                          "3.Tratament specific:\nUn ser cu ingrediente ce ajută la reglarea producției de sebum (ex. niacinamidă) sau o formulă cu retinol în doze mici",
                          "4.Hidratare de noapte:\nO cremă hidratantă puțin mai bogată decât cea de dimineață"
                          ]
            },
            "Sensibilă": {
                "Dimineața": [
                    "\n1.Curățare delicată:\nUn gel sau spumă de curățare non-iritant",
                    "2.Tonifiere/ Balansare pH:\n Un toner cu ingrediente calmante, fara alcool",
                    "3.Ser calmant:\n Un ser cu niacinamida/acid hialuronic",
                    "4.Hidratare:\n O cremă hidratantă hipoalergenică, fără parfumuri și cu panthenol, ceramide",
                    "5.Protecție solară:\n Un produs cu SPF 30/50 cu textură ușoară\n\n"
                ],
                "Seara": ["\n1.Curățare în profunzime (Double Cleanse):\nPrimul pas: Un demachiant pe bază de ulei sau o apă micelară\nAl doilea pas: Un gel sau spumă de curățare delicat, similar cu cel utilizat dimineața.",
                          "2.Tonifiere:\nUn toner cu ingrediente calmante, fara alcool",
                          "3.Tratament specific:\nun ser cu o textură lejeră și ingrediente care reduc roșeața și calmează iritațiile (ex. extract de mușețel, alantoina)",
                          "4.Hidratare de noapte:\nO cremă de noapte mai bogată conceputa special pentru ten sensibil",
                          "5.Masca calmantă (opțional):\no mască hidratantă și calmantă"
                          ]
            }
        }

    def afiseaza_recomandari(self, tip_piele):
        return self.recomandari.get(tip_piele)

    def produse_recomandate(self, tip_piele):

        links = {
            "Grasă": {
                "Dimineața": [
                    "https://skinguru.ro/produs/cosrx-salicylic-acid-daily-gentle-cleanser-150ml-gel-de-curatare-cu-acid-salicilic/",
                    "https://geekandgorgeous.ro/calm-down-100-ml-2-50",
                    "https://geekandgorgeous.ro/c-glow-30-ml-2-58",
                    "https://nuoderm.ro/products/crema-melc",
                    "https://skinguru.ro/produs/beauty-of-joseon-relief-sun-rice-probiotics-50ml-spf50pa/"
                ],
                "Seara": [
                    "https://skinguru.ro/produs/anua-heartleaf-pore-control-cleansing-oil-200ml/",
                    "https://skinguru.ro/produs/cosrx-salicylic-acid-daily-gentle-cleanser-150ml-gel-de-curatare-cu-acid-salicilic/",
                    "https://geekandgorgeous.ro/porefectly-clear",
                    "https://geekandgorgeous.ro/liquid-hydration-110-ml-toner-facial-hidratant",
                    "https://geekandgorgeous.ro/b-bomb-30-ml-2-59",
                    "https://geekandgorgeous.ro/hydration-station-50-ml",
                    "https://www.synergytherm.com/produs/masca-de-fata-pentru-pori-decongestionanta-purifying-face-mask-cu-acid-salicilic-argila-verde-si-argint-coloidal-pentru-curatarea-intensa-a-porilor/"
                ]
            },
            "Uscată": {
                "Dimineața": [
                    "https://www.drmax.ro/gel-de-spalare-hidratant-pentru-piele-normal-uscata-1000ml-cerave",
                    "https://geekandgorgeous.ro/liquid-hydration-110-ml-toner-facial-hidratant",
                    "https://geekandgorgeous.ro/ha-5-rich-30-ml-2-60",
                    "https://www.drmax.ro/crema-reparatoare-pentru-fata-si-corp-13-glicerina-piele-atopica-panthenol-comfort-400ml-mixa",
                    "https://www.drmax.ro/crema-de-fata-hyperpigmentation-defense-p20-spf-50-50ml-riemann"
                ],
                "Seara": [
                    "https://skinguru.ro/produs/anua-heartleaf-pore-control-cleansing-oil-200ml/",
                    "https://www.drmax.ro/gel-de-spalare-hidratant-pentru-piele-normal-uscata-1000ml-cerave",
                    "https://geekandgorgeous.ro/liquid-hydration-110-ml-toner-facial-hidratant",
                    "https://www.synergytherm.com/produs/ser-hidratant-hydrate-serum-ser-cu-3-tipuri-de-acid-hialuronic-si-provitamina-b5-pentru-hidratare-profunda/",
                    "https://www.synergytherm.com/produs/crema-reparatoare-cicatherm/",
                    "https://skinguru.ro/produs/anua-heartleaf-cream-mask-night-solution-pack/"
                ]
            },
            "Mixtă": {
                "Dimineața": [
                    "https://www.synergytherm.com/produs/spuma-curatare-ten-foaming-facial-cleanser-demachiant-tip-spuma-cu-acizi-derivati-din-fructe-aloe-vera-si-panthenol/",
                    "https://skinguru.ro/produs/beauty-of-joseon-glow-replenishing-rice-milk-150ml/?utm_source=google+ads&utm_medium=paid&utm_campaign=S+26+may&gad_source=1&gbraid=0AAAAABOQTaASedK8w1pVcN1wOrGd5omEH&gclid=Cj0KCQjw2ZfABhDBARIsAHFTxGx3mFMMKwQ8Bc9fIFM2ir2g_RIZyWtpGu2m1peGWn9-u3pPX2KNM_UaAgVbEALw_wcB",
                    "https://www.bilenegre.ro/produs/serum-pentru-uniformizare-cu-vitamina-c-23-20g-cosrx/?gad_source=1&gbraid=0AAAAAqCHzLqERy433lMdhbpOxysPchxnS&gclid=Cj0KCQjw2ZfABhDBARIsAHFTxGz2CIOVi9sLK-rl4MjaLVaI05u2CtP6Fm5hqI5WB6PR86k80GAGoWIaAskZEALw_wcB",
                    "https://www.synergytherm.com/produs/ser-seboregulator-radical-skin-reform-serum-ser-cu-niacinamida-retinol-si-acid-hialuronic-echilibreaza-secretia-de-sebum/",
                    "https://www.synergytherm.com/produs/spf50-crema-pentru-fata-daily-use-sunscreen-50-crema-hidratanta-cu-protectie-solara-cu-spectru-larg-ce-protejeaza-impotriva-razelor-uva-uvb/"
                ],
                "Seara": [
                    "https://skinguru.ro/produs/anua-heartleaf-pore-control-cleansing-oil-200ml/",
                    "https://www.synergytherm.com/produs/spuma-curatare-ten-foaming-facial-cleanser-demachiant-tip-spuma-cu-acizi-derivati-din-fructe-aloe-vera-si-panthenol/",
                    "https://geekandgorgeous.ro/liquid-hydration-110-ml-toner-facial-hidratant",
                    "https://geekandgorgeous.ro/a-game20-30-ml",
                    "https://www.drmax.ro/crema-reparatoare-pentru-fata-si-corp-13-glicerina-piele-atopica-panthenol-comfort-400ml-mixa"


                ]
            },
            "Sensibilă": {
                "Dimineața": [
                    "https://www.drmax.ro/gel-de-spalare-hidratant-pentru-piele-normal-uscata-1000ml-cerave",
                    "https://geekandgorgeous.ro/liquid-hydration-110-ml-toner-facial-hidratant",
                    "https://geekandgorgeous.ro/ha-5-rich-30-ml-2-60",
                    "https://www.drmax.ro/crema-reparatoare-pentru-fata-si-corp-13-glicerina-piele-atopica-panthenol-comfort-400ml-mixa",
                    "https://www.drmax.ro/crema-de-fata-hyperpigmentation-defense-p20-spf-50-50ml-riemann"
                ],
                "Seara": [
                    "https://skinguru.ro/produs/anua-heartleaf-pore-control-cleansing-oil-200ml/",
                    "https://www.drmax.ro/gel-de-spalare-hidratant-pentru-piele-normal-uscata-1000ml-cerave",
                    "https://geekandgorgeous.ro/liquid-hydration-110-ml-toner-facial-hidratant",
                    "https://www.synergytherm.com/produs/ser-hidratant-hydrate-serum-ser-cu-3-tipuri-de-acid-hialuronic-si-provitamina-b5-pentru-hidratare-profunda/",
                    "https://www.synergytherm.com/produs/crema-reparatoare-cicatherm/",
                    "https://skinguru.ro/produs/anua-heartleaf-cream-mask-night-solution-pack/"
                ]
            }
        }
        return links.get(tip_piele)