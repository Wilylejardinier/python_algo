### 11. Écrire un programme qui affiche une table de conversion de sommes d’argent exprimées en euros (de 1 euro à 1200 euros), en dollars américains.
#On partira de 1 euro = 1.10 dollars (taux fictif).  
#On affichera donc une table de 1 à 1200 euros convertis.

taux = 1.10  # exemple de taux
for euros in range(1, 1201):
    dollars = euros * taux
    print(euros, "euros =", round(dollars, 2), "dollars")