#Haddouche Darine Aya , BAACHEV , 13/12/2025
#Smahi Ibtissem
#Lakoues Feryal
#Bouklikha Ines


import pandas as pd 
import numpy as np

#Données : Séquence ADN , Longueur , Pourcentage GC
data = { 
    "Séquence":["ATGCGTACGTA", "GCTAGCTAGGCC", "ATGCGCGTAAGT", "TACGATCGTA", "ATGAAAGGCTT", "CGTACGTAGC", "TTAACCGGAT"],
    "Longueur":[12, 12, 12, 10, 11, 10, 10],
    "Pourcentage GC":[50, 66.67, 58.33, 40, 45.45, 60, 50]
}

    
# 1) Créer et afficher le tableau en utilisant pandas 
print("*********** Création et affichage du DataFrame **************")
df = pd.DataFrame(data)


#Affichage Du Tableau 
print ("Tableau De Séquence ADN :")
print (df)
print ("-" * 70)


# 2) Sélectionner et afficher uniquement la colonne "Longueur" ---
print("\n--- Tâche
      

#Affichage de la colonne 'Longueur' ---")
colonne_longueur = df["Longueur"]
print(colonne_longueur)
print("-" * 50)  


# 3) Filtrer les séquences dont la longueur est supérieure à 10 ---
print("\n--- Tâche 3


#Filtrage des séquences de Longueur > 10 ---")
Application du filtre: sélection des lignes où "Longueur" > 10
print("3. Séquences filtrées (Longueur > 10):")
print(df_filtre)
print("-" * 50)


# 4) Calculer le pourcentage moyen de GC avec 3 chiffres après la virgule ---
print("\n--- Tâche 4


#Calcul du Pourcentage Moyen de GC ---")
moyenne_gc = df['Pourcentage GC'].mean()
print(f"4. Moyenne de 'Pourcentage GC': {moyenne_gc:.3f}")
print("-" * 50)


# 5) Ajouter Une Colonne "Catégorie GC"
print ("***********Ajout De La Colonne 'Catégorie GC'***********")

# Définition De La Fonction De Catégorisation
def categorie_gc (pourcentage) :
    if pourcentage > 55:
        return "Riche"
    elif 45 <= pourcentage <= 55:
        return "Moyen"
    else: # pourcentage < 45
        return "Faible"
            
#Application De La Fonction A La Colonne " Pourcentage GC "
df["Catégorie GC"]= df ["Pourcentage GC"].apply (categorie_gc)
print (df)
print("-" * 70)

      
