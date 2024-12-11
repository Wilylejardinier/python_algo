### 2. Saisir un entier `N` et vérifier s’il est pair ou impair en utilisant l’opérateur modulo `%`.

N = int(input("Entrez un entier : "))
if N % 2 == 0:
    print(N, "est pair.")
else:
    print(N, "est impair.")