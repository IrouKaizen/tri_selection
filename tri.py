def sort_array(array):
    # Boucle externe pour parcourir tous les éléments de la liste
    for i in range(len(array) - 1):
        # Boucle interne pour comparer chaque paire d'éléments
        for j in range(len(array) - i - 1):
            # Si l'élément actuel est plus grand que le suivant, les échanger
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

# Demande à l'utilisateur de saisir le nombre d'éléments
length = int(input("Entrez le nombre d'éléments : "))

# Initialise la liste pour stocker les entrées de l'utilisateur
array = []

# Demande à l'utilisateur de saisir les éléments
print("Entrez les éléments : ")
for i in range(length):
    value = input()
    # Vérifie si la valeur est un nombre entier
    if value.isdigit():
        array.append(int(value))
    else:
        # Si ce n'est pas un nombre entier, demande à l'utilisateur de ressaisir
        print("Entrée incorrecte, veuillez entrer un nombre : ")
        i -= 1

# Trie la liste d'entiers
sort_array(array)

# Affiche la liste triée
print("La liste triée :", array)
