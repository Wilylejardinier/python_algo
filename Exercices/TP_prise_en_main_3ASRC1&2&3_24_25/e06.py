### 6. Afficher les entiers compris entre 1 et 10 compris, puis utiliser l’instruction `break/continue` pour la variable de boucle égale à 8.

for i in range(1, 11):
    if i == 8:
        continue  # on saute l'affichage de 8 ou break pour stopper à 8
    print(i)
