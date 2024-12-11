### 3. Saisir un entier `N` et vérifier s’il est positif, négatif ou nul.

N = int(input("Entrez un entier : "))
if N > 0:
    print(N, "est positif.")
elif N < 0:
    print(N, "est négatif.")
else:
    print("Le nombre est nul.")