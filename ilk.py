print("Merhaba")
liste = ["ibrahim",
         "pehlivan",
         "seher","abdullah",
         "yunus",
         "fatih","murat" ,"cagatay"]
import os
filename="deneme.ipynb"
for item in liste:
    if not os.path.exists(os.path.join("Egzersizler",item)):
        os.mkdir(os.path.join("Egzersizler",item))
    open(os.path.join("Egzersizler",item,filename),"w")
