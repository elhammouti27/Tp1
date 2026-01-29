from produit import Produit, ProduitAlimentaire, ProduitElectronique
class Inventaire:
    def __init__(self):
        self.produits = []


    def ajouter(self, produit):
        if not isinstance(produit, Produit):
            raise ValueError("error, c'est pas un produit !")
        self.produits.append(produit)

    
    def total_frais_livraison(self):
        pass


    def lister_par_type(type_classe):
        pass


    def produits_perimes(self):
        pass


inv = Inventaire()
p = ProduitElectronique("KB-001", "Clavier", 79.99, 15, 24, 0.5)
inv.ajouter(p)
inv.ajouter(ProduitElectronique("SC-001", "Écran", 299.99, 5, 36, 5.0))
inv.ajouter(ProduitAlimentaire("ALI-001", "Comté", 12.99, 50, "2025-06-15"))
inv.ajouter(ProduitAlimentaire("ALI-002", "Lait", 1.50, 100, "2024-01-01"))  # Périmé

#print(inv.total_frais_livraison())  # 51.0 (11 + 20 + 15 + 15)
#print(len(inv.lister_par_type(ProduitElectronique)))  # 2
#print(len(inv.produits_perimes()))  # 1 (le lait)