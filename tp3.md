# TP3 : Produit encapsulé pour PyInventory

## Objectif

Appliquer l'encapsulation complète à la classe Produit de PyInventory.

## Instructions

- Reprenez la classe Produit du Jour 1
- Transformez tous les attributs en attributs protégés (`_`)
- Créez des propriétés avec validation pour :
  - `reference` : chaîne de 3+ caractères, convertie en majuscules
  - `nom` : chaîne de 2+ caractères
  - `prix_ht` : nombre positif, arrondi à 2 décimales
  - `stock` : entier positif ou nul
- Ajoutez les propriétés calculées : `prix_ttc`, `valeur_stock`
- Ajoutez les méthodes : `ajouter_stock()`, `retirer_stock()`

## Tests à exécuter

```python
p = Produit("kb-001", "Clavier RGB", 79.99, 15)
print(p.reference)    # KB-001 (converti en majuscules)
print(p.prix_ttc)     # 95.99

p.prix_ht = 69.99     # OK
p.ajouter_stock(10)   # Stock: 25
p.retirer_stock(5)    # Stock: 20

# Ces lignes doivent lever des exceptions
# p.prix_ht = -10     # ValueError
# p.stock = 5.5       # TypeError
# p.reference = "ab"  # ValueError (trop court)
```

## Indices

- Dans le constructeur, utilisez `self.attribut = valeur` (pas `self._attribut`) pour déclencher les setters
- Utilisez `isinstance(valeur, (int, float))` pour vérifier les nombres
- N'oubliez pas `round(valeur, 2)` pour les prix