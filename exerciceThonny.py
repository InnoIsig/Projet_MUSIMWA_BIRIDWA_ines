pays = input("Entrez le pays\n")
visites = int(input("Entrez le nombre de pays vistés\n"))
liste_de_villes = eval(input("Entrez la liste de villes visitées\n"))

traval_log = [
    {
        "Pays": "France",
        "Visite": 3,
        "Villes": ["Paris", "Dijon", "Marselle"]
    },
    {
        "Pays": "RDC",
        "Visite": 3,
        "Villes": ["Kinshasa", "Goma", "Bunia"]
    },

]

def ajouter_nouveau_pays(nom, nombre_visite, ville_viiste):
    nouveau_pays = {}
    nouveau_pays["Pays"] = nom
    nouveau_pays["Vistes"] = nombre_visite 
    nouveau_pays["Villes"] = ville_viiste
    traval_log.append(nouveau_pays)

ajouter_nouveau_pays(pays, visites, liste_de_villes)
print(f"J'ai été à {traval_log[2]['Pays']} {traval_log[2]['Vistes']} temps")
print(f"Mes villes préférées étaient {traval_log[2]['Villes'][0]}")
