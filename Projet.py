# 3. Filtrer les séquences dont la longueur est supérieure à 10.
df_filtre = df[df['Longueur'] > 10]
print("3. Séquences filtrées (Longueur > 10):")
print(df_filtre)
print("-" * 50)

# 4. Calculer le pourcentage moyen de GC avec 3 chiffres après la virgule.
moyenne_gc = df['Pourcentage GC'].mean()
print(f"4. Moyenne de 'Pourcentage GC': {moyenne_gc:.3f}")
print("-" * 50)# Baachev_Darine-Haddouche
