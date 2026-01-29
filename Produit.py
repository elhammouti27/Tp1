from abc import ABC, abstractmethod
from datetime import date
class Produit:

    _tva = 0.20
    _nb_produits = 0
    def __init__(self, reference , nom, prix_ht, stock):
        self.reference = reference
        self.nom = nom
        self.prix_ht = prix_ht
        self.stock = stock 
        Produit._nb_produits += 1



    @property
    def reference(self):
        return self._reference 
    
    @reference.setter
    def reference(self, reference):
        if len(reference) <= 3 :
            raise ValueError("reference doit contenir plus de 3 caracter")
        self._reference = reference.upper()
    @property
    def nom(self):
        return self._nom
    
    @nom.setter
    def nom(self, value):
        if len(value) <= 2 :
            raise ValueError("le nom de produit trop court")
        self._nom = value
    
    @property
    def prix_ht(self):
        return self._prix_ht
    

    @prix_ht.setter
    def prix_ht(self, value):
        if value < 0 :
            raise ValueError("Invalide nombre")
        self._prix_ht = round(value, 2)
    
    @property
    def stock(self):
        return self._stock
    
    @stock.setter
    def stock(self, value):
        if value < 0 :
            raise ValueError("Error") 
        self._stock = value

    @property
    def prix_ttc(self):
        return self.prix_ht * (1 + Produit._tva / 100)

    def afficher(self):
        print(f"Référence: {self.reference}, Nom: {self.nom}, Prix HT: {self.prix_ht}, Stock: {self.stock}")

    def est_disponible(self):
        if self.stock > 0:
            return True
        else:
            return False

    def ajouter_stock(self, quantite):
        self.stock = self.stock + quantite
        return self.stock

    def retirer_stock(self, quantite):
        self.stock = self.stock - quantite
        return self.stock

    def valeur_stock(self):
        return self.stock * self.prix_ht
    


    @abstractmethod
    def calculer_frais_livraison():
        pass

    @abstractmethod
    def afficher_details():
        pass


class ProduitElectronique(Produit):
    def __init__(self, reference, nom, prix_ht, stock, garantie_mois, poids_kg):
        super().__init__(reference, nom, prix_ht, stock)
        self.garantie_mois = garantie_mois
        self.poids_kg = poids_kg
    
    @property
    def garantie_mois(self):
        return self._garantie_mois
    
    @garantie_mois.setter
    def garantie_mois(self, value):
        if not isinstance(value, int):
            raise ValueError("error")
        self._garantie_mois = value



    @property
    def poids_kg(self):
        return self._poids_kg
    
    @poids_kg.setter
    def poids_kg(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("error")
        self._poids_kg = value


    def calculer_frais_livraison(self):
        # Frais = 10€ + 2€ par kg
        return 10 + 2 * self.poids_kg

    def afficher_details(self):
        print(f" Garantie {self.garantie_mois} mois | poids : {self._poids_kg}")
        



class ProduitAlimentaire(Produit):
    frais_livraison = 15
    def __init__(self, reference, nom, prix_ht, stock, date_peremption):
        super().__init__(reference, nom, prix_ht, stock)
        self.date_peremption = date_peremption

    
    @property
    def date_peremption(self):
        return self._date_peremption
    
    @date_peremption.setter
    def date_peremption(self, value):
        try:
            self._date_peremption = date.fromisoformat(value)
        except ValueError:
            raise ValueError("error de date")




    def est_perime(self):
        return date.today() > self.date_peremption
        
    def afficher_details(self):
        print(f" Date de peremption : {self.date_peremption} €")


    def calculer_frais_livraison(self):
        return ProduitAlimentaire.frais_livraison
    


