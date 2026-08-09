import pandas as pd
import glob
import re 
from unidecode import unidecode

def main ():
    files = glob.glob("D:\projet_darija/BDD_darija/*.xlsx")
    dataset_global= []
    # garder seulement les colonnes "n1" & "fren"
    for f in files:
        df = pd.read_excel(f)
        df= df [["n1","fren"]]
        dataset_global.append(df)
    # fusionner tous les fichiers 
    fusion=pd.concat(dataset_global, ignore_index=True)
    
    #Verification avant d'avancer 
    fusion.to_excel("D:\projet_darija/data/processed/dataset_preview.xlsx", index=False)

main()
# Nettoyage (supprimer les doublons, les valeurs manquantes et nettoyage de texte )
fusion= pd.read_excel(r"D:\projet_darija\data\processed\dataset_preview.xlsx")
print(fusion.head())
fusion.drop_duplicates(inplace=True)
fusion.dropna(inplace=True)

def nettoyage_texte(texte):
  if pd.isnull(texte): 
     return " "
  if isinstance(texte, str):
   texte=texte.lower()
   texte=re.sub(r'[^a-zA-Z0-9\u00C0-\u017F\u0600-\u06FF\s]', '', texte)
   texte=re.sub(r'\s+',' ',texte).strip()
   return texte

fusion=fusion.applymap(nettoyage_texte)
fusion.to_excel("D:\projet_darija/data/processed/dataset_preview.xlsx", index=False)
