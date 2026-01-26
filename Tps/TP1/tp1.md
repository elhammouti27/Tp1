# TP1 : Classe Produit pour PyInventory

## Objectif

Créer la classe Produit de base pour le projet PyInventory.

## Attributs d'instance

- `reference` : code unique du produit (ex: "KB-001")
- `nom` : nom du produit
- `prix_ht` : prix hors taxes
- `stock` : quantité en stock

## Attributs de classe

- `tva` : taux de TVA (20% par défaut)
- `nb_produits` : compteur de produits créés

## Méthodes

- `prix_ttc()` : retourne le prix TTC
- `afficher()` : affiche les informations du produit
- `est_disponible()` : retourne True si stock > 0
- `ajouter_stock(quantite)` : ajoute au stock
- `retirer_stock(quantite)` : retire du stock (si possible)
- `valeur_stock()` : retourne prix_ht * stock

## Exemple d'utilisation

```python
p1 = Produit("KB-001", "Clavier mécanique RGB", 79.99, 15)
p2 = Produit("MS-002", "Souris gaming 16000 DPI", 49.99, 25)

p1.afficher()
# Réf: KB-001 | Clavier mécanique RGB | 79.99€ HT (95.99€ TTC) | Stock: 15

print(f"Valeur du stock: {p1.valeur_stock()}€")  # 1199.85€
p1.retirer_stock(3)   # Stock retiré: 3. Nouveau stock: 12
p1.retirer_stock(20)  # Stock insuffisant

print(f"Total produits: {Produit.nb_produits}")  # 2
```

## Indices

- Prix TTC : `self.prix_ht * (1 + Produit.tva / 100)`
- Utilisez les f-strings pour l'affichage
- Vérifiez que la quantité à retirer ne dépasse pas le stock