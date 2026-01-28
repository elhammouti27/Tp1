#from Categorie import Categorie
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
        self._prix_ht = value
    
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
    


p = Produit("kb-gg1", "ADB", 79.99, 15)
print(p.reference)  # KB-001 (converti en majuscules)
#print(p.prix_ttc)

print(p.nom)
print(p.prix_ttc)

p.prix_ht = 69.99     # OK
p.ajouter_stock(10)