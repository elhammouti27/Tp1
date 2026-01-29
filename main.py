from produit import ProduitAlimentaire , ProduitElectronique


clavier = ProduitElectronique("KB-001", "Clavier RGB", 79.99, 15, 24, 0.5)
fromage = ProduitAlimentaire("ALI-001", "Comté", 12.99, 50, "2025-06-15")

print(clavier.calculer_frais_livraison())  # 11.0 (10 + 0.5*2)
print(fromage.calculer_frais_livraison())  # 15.0

clavier.afficher_details()  # Garantie: 24 mois, Poids: 0.5kg
fromage.afficher_details()  # Péremption: 2025-06-15

print(fromage.est_perime())  # False (ou True selon la date)

