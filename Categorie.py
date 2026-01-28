from Produit import Produit
class Categorie:
    def __init__(self, nom , description):
        self.nom = nom
        self.description = description
        self.produits = []

    def ajouter_produit(self, produit):
        return self.produits.append(produit)
    
    def retirer_produit(self, reference):
        for produit in self.produits:
           return self.produits.remove(produit)
    
    def lister_produit(self):
        print(f"Liste des produits dans la catégorie {self.nom} :  {self.produits}")

    def nb_produits(self):
        return len(self.produits)
    
    def valeur_totale(self):
        pass 


    