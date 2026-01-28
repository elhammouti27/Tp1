class Produit:

    tva = 0.20
    nb_produits = 0
    def __init__(self, reference , nom, prix_ht, stock):
        self.reference = reference
        self.nom = nom
        self.prix_ht = prix_ht
        self.stock = stock 


    def prix_ttc(self):
        return self.prix_ht * (1 + Produit.tva / 100)

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
    

p1 = Produit("KB-001", "Clavier mécanique RGB", 79.99, 15)
p2 = Produit("MS-002", "Souris gaming 16000 DPI", 49.99, 25)
p3 = Produit("EC-003", "Écran 27 pouces 4K", 399.99, 10)

p1.afficher()
  
p1.ajouter_stock(5)    

p1.afficher()

p1.retirer_stock(2)

p1.afficher()