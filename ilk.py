liste = ["ibrahim",
         "pehlivan",
         "seher","abdullah",
         "yunus",
         "fatih","murat" ,"cagatay"]
import os
import shutil
filename="01_pandas.ipynb"
for item in liste:
    if not os.path.exists(os.path.join("Egzersizler",item)):
        os.mkdir(os.path.join("Egzersizler",item))
    if not os.path.exists(os.path.join("Egzersizler",item,"data")):
        os.mkdir(os.path.join("Egzersizler",item,"data"))
    srcPath = "/workspace/pythonfundamentals/Dokumanlar/04_Libraries/data/pokemon.csv"
    destPath = fr"/workspace/pythonfundamentals/Egzersizler/{item}/data/pokemon.csv"
    shutil.copy(srcPath,destPath)
    open(os.path.join("Egzersizler",item,filename),"w")
