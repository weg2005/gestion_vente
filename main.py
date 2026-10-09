# main.py

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from screens.inscription import PageInscription
from screens.saisifacture import SaisiFacture
from screens.connexion import PageConnexion
from screens.acceil import PageAcceil
from screens.caisse import PageCaisse
from database.user_db import count_users
from screens.tableau_bord import TableauBord
from screens.versement import ScreenVersement
from screens.creation_compte_vers import CreationCompteVers
from screens.creer_article import CreerArticle
from screens.enregistrement_BL import Enregistrer_BL 
from screens.enregistrement_fact import Enregistrer_Fact
from screens.sorti_stock_fne import SortiFNE
from screens.sorti_stock_bl import SortiBL
from screens.sorti_stock_pr import SortiPR
from screens.avoir_facture import AvoirFacture
from screens.gestion_stock import GestionStock
from screens.commande import Commande
from screens.impression import PageImpression_BL
from screens.impression_fact import PageImpression_Fact
from screens.inventaire_tournant import InventaireTournant
from screens.inventaire_anuel import InventaireAnuel

class MyApp(App):
    
    def build(self):
        smg = ScreenManager()

        # Si la base est vide, on force la création d'un compte Admin#
        
        if count_users() == 0:
            smg.add_widget(PageInscription(name='inscription'))

        smg.add_widget(PageConnexion(name='connexion'))
        smg.add_widget(PageAcceil(name='acceil'))
        smg.add_widget(PageCaisse(name='page_caisse'))
        smg.add_widget(SaisiFacture(name='Saisi_Facture'))
        smg.add_widget(TableauBord(name = "TableauBord"))
        smg.add_widget(ScreenVersement(name = "ScreenVersement"))
        smg.add_widget ( CreationCompteVers(name = "CreationCompteVers"))
        smg.add_widget(CreerArticle(name = "CreerArticle"))
        smg.add_widget (Enregistrer_BL (name = 'Enregistrer_BL'))
        smg.add_widget (Enregistrer_Fact (name = 'Enregistrer_Fact'))
        smg.add_widget(SortiFNE(name = 'SortiFNE'))
        smg.add_widget(SortiBL(name = 'SortiBL'))
        smg.add_widget(SortiPR(name = 'SortiPR'))
        smg.add_widget(AvoirFacture(name = 'AvoirFacture'))
        smg.add_widget(GestionStock(name = 'GestionStock'))
        smg.add_widget(Commande(name = 'Commande'))
        smg.add_widget(PageImpression_BL(name = 'PageImpression_BL'))  
        smg.add_widget(PageImpression_Fact(name = 'PageImpression_Fact'))
        smg.add_widget(InventaireTournant(name = 'inventairetournant'))
        smg.add_widget(InventaireAnuel(name = 'inventaireanuel'))

        return smg

if __name__ == "__main__" :
    MyApp().run()
