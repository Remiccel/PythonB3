liste_tache = []
liste_termine = []
status = True

def ajout():
    taches = input("Entrez les nouvelles tâches séparées par une virgule : ")
    nouvelles_taches = [t.strip() for t in taches.split(',')]                    #découpe si plusieurs tache renseignée
    liste_tache.extend(nouvelles_taches)                                         
    print("Vos tâches ont bien été ajoutées.")

def supprimer():
    taches_a_supp = input("Entrez les tâches à supprimer séparées par une virgule : ")
    taches_a_supp = [t.strip() for t in taches_a_supp.split(',')]
    
    for tache in taches_a_supp:
        if tache in liste_tache:
            liste_tache.remove(tache)
            print(f"Votre tâche '{tache}' a bien été supprimée.")
        else:
            print(f"La tâche '{tache}' que vous voulez supprimer n'existe pas.")


def MaJ ():
    print ("Après mise à jour, il reste ces tâches à faire", liste_tache)


def termine():
    o = input('Quelle tâche avez-vous terminer ? ')
    liste_termine.append(o)
    print('Les tâches terminées sont : ',liste_termine)


while status == True : 
    a= input('Que souhaitez vous faire ? \n########################## \n - ajout \n - supprimer \n - MaJ \n - terminée \n  veuillez ajoutez ici-->')
    if a == 'ajout':
        ajout()
        continue
    elif a == 'supprimer':
        supprimer()
    elif a == 'MaJ':
        MaJ()
    elif a == 'terminée':
        termine()
    else :
        break
    

