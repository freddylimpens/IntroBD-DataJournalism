# Enoncé

Récupérez le fichier `exam2016.db.sqlite` dans le dossier `exam2016` [du dépôt du cours](https://github.com/freddylimpens/IntroBD-DataJournalism) et chargez le dans SQLiteMan. Vous verrez les 4 tables utilisées dans cet examen:

1. `surf_bio_evol`
2. `population_dpt`
3. `exp_surf_bio_2012`
4. `distributeurs`

Reprenez l'énoncé de l'examen dans un éditeur de texte de votre choix. Chaque question attend une réponse sous la forme d'une requête SQL. Testez vos requêtes sous SQLiteMan, et recopiez les requêtes SQL permettant de répondre à la question sous chacune des questions.

Chaque question est notée sur 1 point.

Remettez ensuite ce fichier dans le devoir "Examen Partiel" sur le [site Moodle du cours](http://moodle.univ-lille3.fr/course/view.php?id=4904)

Si vous rencontrez des difficultés, envoyez le fichier réponse par email `freddy.limpens@univ-lille3.fr`


# Surface bio et SAU (Surface Agricole Utile) des départements français

La table `surf_bio_evol` donne l'identifiant (`id_departement`) et le nom de département (`nom_departement`), la surface bio (`surf_bio_2001`, `surf_bio_2012`), et la SAU (Surface Agricole Utile `sau_2001` et `sau_2012`) des départements français pour les années 2001 et 2012

## Question 1
Donnez le nom de département, la SAU 2001, et la SAU 2012 des départements de la région Hauts de France (aidez vous de wikipedia au besoin pour avoir cette liste), ordonnés par SAU de 2001 descendante


## Question 2
Toujours pour les départements des Hauts de France, affichez le nom et la différence entre la SAU 2012 et la SAU 2001 (celle de 2001 moins celle de 2012), ordonnez les départements par ordre de différence décroissante (de celui qui a perdu le plus vers celui qui a perdu le moins)


## Question 3
Y'a t'il des départements, au niveau de la France entière à présent, dont la SAU a augmenté entre 2001 et 2012 ? Donnez leur liste et la différence de SAU.


## Question 4
Donnez la liste des départements dont la surface bio 2012 est comprise entre 20000 et 50000 ha. Ordonnez par surface décroissante.


## Question 5
Y'a t'il des départements dont la surface bio a baissé entre 2001 et 2012 ? Donnez une requête permettant de le vérifier.


## Question 6
Donnez le nom et le pourcentage de surface bio par rapport à la SAU, pour tous les départements de France en excluant seulement le département des HAUTS-DE-SEINE. Ordonnez par pourcentage décroissant.


# Population des départements français

La table `population_dpt` donne le nom de région (`region`), l'identifiant (`id_departement`) et le nom (`nom_departement`), le nombre de communes (`nb_communes`) et la population (`population`) pour les départements français.

## Question 7
Donnez le nom de département, le nombre de commune, et la population des départements appartenant à la région Hauts de France.


## Question 8
Donnez le nom de département, le nombre de commune, et la population des départements dont le nom de région commence par la lettre 'P' ou par la lettre 'N'

## Question 9
En utilisant une fusion avec la table `surf_bio_evol`, donnez pour chaque département : son nom, et le nombre d'hectare de SAU pour 10 habitants. Ordonnez selon cette valeur de manière décroissante.



# Surface et Nombre d'exploitants bio des départements français

Voir le tableau `exp_surf_bio_2012` mettant en lien le nombre d'exploitants bio (`nb_exp_bio`) et surface bio(`surf_bio`) par département (`id_departement`) pour l'année 2012

## Question 10
Donnez l'id du département et le nombre d'exploitants bio, classés par ordre décroissant, et pour les 10 premiers départements


## Question 11
Donnez l'id du département et la surface moyenne par exploitation pour chaque département (c'est un ratio). Ordonnez les départements par surface moyenne décroissante, et n'affichez que les 10 premiers.


## Question 12
Refaites le même calcul, mais en affichant le nom du département au lieu de son identifiant en effectuant une fusion avec la table `population_dpt`


## Question 13
En fusionnant les mêmes tables `population_dpt` et `exp_surf_bio_2012`, donnez maintenant le nom de département et le nombre d'exploitants bio pour 10 000 habitants pour chaque département (la formule correspond à un produit en croix); ordonner selon cette valeur par ordre décroissant.


# Table `distributeurs`
Cette table donne le nombre de distributeurs bio par département en 2011 (pour les comparaisons avec les autres tables on supposera que ce nombre a faiblement évolué en 2012).

## Question 14
Calculez la valeur moyenne du nombre de distributeurs arondie à l'entier (sans décimale)


## Question 15
Créez une table appelée `resultats` comprenant 2 colonnes: 1 appelé `variable`, contenant du texte, l'autre appelé `valeur` et contenant un nombre entier.


## Question 16
Insérez dans cette table nouvellement créée la valeur calculée précédemment en lui donnant le nom de votre choix (si vous n'avez pas réussi à la calculer, donnez une valeur arbitraire).



## Question 17
Donnez une requête permettant de **compter** les départements dont le nombre de distributeurs est supérieur à la moyenne précédemment calculée (utilisez une valeur arbitraire sinon)



## Question 18
Donnez le nom de région, et la somme des distributeurs pour chaque région, ordonnez les régions par nombre décroissant de distributeurs bio.



## Question 19
A l'aide d'une fusion avec la table `exp_surf_bio_2012`, donnez le nom de département et le nombre de producteur par distributeurs (ratio) pour chaque département. Ordonnez les valeurs par ordre décroissant de ce ratio.


## Question 20
A l'aide d'une fusion avec la table `population_dpt`, afficher maintenant pour tous les départements leur nom et le nombre de distributeurs pour 100 000 habitants (toujours un produit en croix)
