#Haddouche Darine Aya , BAACHEV , 13/12/2025
#Semahi Ibtisam
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
      
