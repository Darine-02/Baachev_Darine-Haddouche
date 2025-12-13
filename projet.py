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


# 2) Sélectionner et afficher uniquement la colonne "Longueur" 
print("************ Affichage De La Colonne 'Longueur' *************")
Longueur = df["Longueur"]
print(Longueur)
print("-" * 70)  


# 3) Filtrer les séquences dont la longueur est supérieure à 10
print("*************** Sequences De Longueur > 10 ****************")

#Application du filtre: sélection des lignes où "Longueur" > 10
df_filtered = df[df["Longueur"] > 10] 
print(df_filtered)
print("-" * 70)


# 4) Calculer Le Pourcentage Moyen De GC Avec 3 Chiffres Après La Virgule
print("************ Calcul Du Pourcentage Moyen De GC ****************")
average_gc = df["Pourcentage GC"].mean()
print(f"Pourcentage moyen de GC : {average_gc:.3f}%")
print("-" * 70)



# 5) Ajouter Une Colonne "Catégorie GC"
print ("*********** Ajout De La Colonne 'Catégorie GC'***********")

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

      
# 6) Ajouter Une Colonne Donnant Le Nombre De 'G' Dans Chaque Séquence
print("*************** Ajout De La Colonne 'Nombre De G'**********")

#Utilisation D'une Fonction Lambda Avec La Méthode .str.count() Pour Compter Les 'G' Dans La Colonne "Séquence"
df["Nombre de G"] = df["Séquence"].apply(lambda seq: seq.count('G'))
print(df[["Séquence", "Nombre de G"]])
print("-" * 70)


# 7) Calculer L'écart Type Du %GC Et De La Longueur Des sSquences
print("*************** Calcul De L'ecart Type ********************")
#Calcul De l'Écart Ttype Du Pour Chaque Colonne Demandée En Utilisant .std()
std_gc = df["Pourcentage GC"].std().round (4)
std_longueur =df["Longueur"].std().round(4)
print (f"écart type du %GC: {std_gc}")
print (f"écart type de la Longueur : {std_longueur}")
print("-" * 70)


# 8) Sauvegarder Le Tableau Final Dans Un Fichier CSV ---
print("********** Sauvegarde Du DataFrame Final En CSV ******************")
df.to_csv("tableau_de_sequences_ADN.csv", index=False)
