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
print("\n--- Tâche)
      

#Affichage de la colonne 'Longueur' ---")
colonne_longueur = df["Longueur"]
print(colonne_longueur)
print("-" * 50)  


# 3) Filtrer les séquences dont la longueur est supérieure à 10 ---
print("\n--- Tâche 3)


#Filtrage des séquences de Longueur > 10 ---")
Application du filtre: sélection des lignes où "Longueur" > 10
print("3. Séquences filtrées (Longueur > 10):")
print(df_filtre)
print("-" * 50)


# 4) Calculer le pourcentage moyen de GC avec 3 chiffres après la virgule ---
print("\n--- Tâche 4)


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

      
# 6)Ajouter une colonne donnant le nombre de 'G' dans chaque séquence ---
print("\n--- Tâche 6: Ajout de la colonne 'Nombre de G' ---")


#Utilisation d'une fonction lambda avec la méthode .str.count() pour compter les 'G' dans la colonne "Séquence"
df["Nombre de G"] = df["Séquence"].apply(lambda seq: seq.count('G'))
print(df[["Séquence", "Nombre de G"]])
print("-" * 50)


# 7)Calculer l'écart-type du %GC et de la longueur des séquences ---
print("\n--- Tâche)
Calcul de l'Écart-type (Std Dev) ---")


#Calcul de l'écart-type (Standard Deviation)
std_gc = df["Pourcentage GC"].std()
std_longueur = df["Longueur"].std()

#Arrondi pour l'affichage (optionnel, mais recommandé pour la clarté)
std_gc_arrondi = round(std_gc, 3)
std_longueur_arrondi = round(std_longueur, 3)

print(f"Écart-type du Pourcentage GC: {std_gc_arrondi}")
print(f"Écart-type de la Longueur: {std_longueur_arrondi}")
print("-" * 50)


# 8)Sauvegarder le tableau final dans un fichier CSV ---
print("\n--- Tâche)
Sauvegarde du Tableau Final en CSV ---")


#Nom du fichier basé sur les consignes
nom_fichier_csv = "Master_chef_projet_Analyse_ADN_Final.csv"

#Sauvegarde du DataFrame complet dans un fichier CSV
#index=False pour ne pas inclure l'index de pandas dans le fichier CSV
df.to_csv(nom_fichier_csv, index=False)

print(f"Le tableau final a été sauvegardé dans le fichier: {nom_fichier_csv}")
print("-" * 50)

#Affichage du tableau final complet pour vérification
print("\n--- Tableau Final Complet ---")
print(df)
