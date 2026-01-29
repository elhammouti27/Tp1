# TP5 : Hiérarchie de produits pour PyInventory

## Objectif

Créer une hiérarchie de classes pour les produits de PyInventory.

## Instructions

- Transformez Produit en classe abstraite avec :
  - Méthode abstraite `calculer_frais_livraison()`
  - Méthode abstraite `afficher_details()`
- Créez `ProduitElectronique(Produit)` avec :
  - Attribut supplémentaire : `garantie_mois`
  - Frais de livraison : 10€ + 2€ par kg
  - Attribut : `poids_kg`
- Créez `ProduitAlimentaire(Produit)` avec :
  - Attribut supplémentaire : `date_peremption`
  - Frais de livraison : 15€ (réfrigéré)
  - Méthode : `est_perime()` qui retourne True si daté

## Tests à exécuter

```python
clavier = ProduitElectronique("KB-001", "Clavier RGB", 79.99, 15, 24, 0.5)
fromage = ProduitAlimentaire("ALI-001", "Comté", 12.99, 50, "2025-06-15")

print(clavier.calculer_frais_livraison())  # 11.0 (10 + 0.5*2)
print(fromage.calculer_frais_livraison())  # 15.0

clavier.afficher_details()  # Garantie: 24 mois, Poids: 0.5kg
fromage.afficher_details()  # Péremption: 2025-06-15

print(fromage.est_perime())  # False (ou True selon la date)
```

## Indices

- Utilisez `from datetime import date` pour les dates
- `date.fromisoformat("2025-06-15")` pour convertir une chaîne
- `est_perime(): return self._date_peremption < date.today()`