# Enoncé

Récupérez le fichier "exam_DB.sqlite" et chargez le dans SQLiteMan. Vous verrez les 4 tables utilisées dans cet examen.
Reprenez l'énoncé de l'examen dans un éditeur de texte de votre choix, et recopiez les requêtes SQL permettant de répondre à la question, sous chacune des questions. 
Remettez ensuite ce fichier dans le devoir "Examen de fin de semestre" sur le site Moodle du cours:
http://moodle.univ-lille3.fr/course/view.php?id=4904

Si vous rencontrez des difficultés, envoyez le fichier réponse par email `freddy.limpens@univ-lille3.fr`

# Présentation des tables

## 1 "isf_france"
visible à l'adresse https://github.com/freddylimpens/IntroBD-DataJournalism/blob/master/exam/isf_france_2009.csv
Base de données ISF (Impôt de Solidarité sur la Fortune)
- Pour l'ANNEE 2009
- pour les Villes de plus de 20 000 habitants ayant plus de 50 redevables à l'ISF

## 2 "idh_npdc" 
visible à l'adresse https://github.com/freddylimpens/IntroBD-DataJournalism/blob/master/exam/idh_npdc_2009.csv
Indice de Développement Humain calculé (année 2009) pour les communes de la région Nord - Pas de Calais

## 3 "population"
https://github.com/freddylimpens/IntroBD-DataJournalism/blob/master/exam/population_france.csv
Population des communes de France de plus de 20 000 habitants (2009)

## 4 Fusion des tables "population" et "isf_france"
https://github.com/freddylimpens/IntroBD-DataJournalism/blob/master/exam/isf_population.csv
Avec les champs:
- commune 
- nb_redevables
- population

# 1. Exercices sur la table "isf_france"
 
## 1
Donner le nombre de communes concernées par cette table

## 2
Donner la liste des communes ayant un nombre de contribuables ISF supérieur à 1000 personnes

## 3
Donner la liste des communes, et la patrimoine moyen des contribuables à l'ISF dont le patrimoine moyen est supérieur à 2,000,000 €?

## 4
Donner la liste des communes dont le nombre de redevables est inférieur à 1000 et le patrimoine moyen supérieur à 2500000€?

## 5
Même question, mais en classant les villes par patrimoine moyen en ordre décroissant

## 6
le mot clé LIMIT ajouté à la fin d'une requête permet de limiter le nombre de résultat. 
En ajoutant par exemple LIMIT 10 aux requêtes précédentes, vous limiterez le nombre de communes résultantes à 10 
 Fort de cette nouvelle connaissance, donner la liste des 20 communes les plus "riches", c'est à dire avec les patrimoines moyens les plus élevés.
 
## 7
Même question, mais en excluant la ville de PARIS

## 8
Donner le nombre de villes comprenant des redevables à l'ISF dans le département du NORD; 


## 9
Idem, mais dans le département du PAS DE CALAIS; 

## 10
Effacer de cette table les valeurs pour la région "Centre"

## 11
Proposer une requête pour vérifier que les valeurs ont bien été effacées 


# Table Indice de développement humain "idh_npdc"

## 12
 Donner les 30 premières villes classées par idh du plus au moins élevé
 
## 13
Donner l'idh et le nom de commune pour les villes suivantes: Lille, Tourcoing, Roubaix, Croix, La Madeleine

## 14
créez une table nommée mon_idh et contenant 2 colonnes, une pour le nom des communes, l'autre pour la valeur de l'idh (nombre à virgule)

## 15
Insérez dans cette table les valeurs relevées ci-dessus pour les villes de Lille, Tourcoing, Roubaix, Croix, La Madeleine

## 16
Donner les villes qui ont un idh supérieur à 0.750


## 17
Parmis ces villes, combien sont situées dnas le département du Nord ? Indice: vous pouvez soit considérer le code postal comme un nombre (compris entre 59000 et 59999) ou une chaine de charactère commençant par '59'.


## 18
Combien dans le département du Pas de Calais 


# Table population

# 19
Donner le nom de commune, la population pour les villes de plus de 20 000 habitants du Nord et du Pas de Calais. Ordonnez par nombre d'habitants, dans l'ordre décroissant

## 20
Combien y'a t-il de ville de plus de 100 000 habitants en France ?


## 21
Combien de villes de plus de 100 000 habitants dans la région Nord - PAs de Calais ?

# Fusions

## 22
Proposez une fusion entre la table Indice de développement humain "idh_npdc" et la table "population"

## 23
Sur la base de cette fusion, proposer un classement des villes du Nord Pas de Calais de plus de 30000 habitants, classées apr idh descendant (indice: écrivez les contraintes de filtrage et d'ordre *après* les règles de fusion)

## 24
Proposer une requête pour faire la fusion entre la table "isf_france" et la table "population". L'objectif de cette fusion est d'obtenir une table comportant les colonnes suivantes:
- nom de la commune
- nombre de redevables à l'ISF
- population de la commune  

## 25
Suite à cette requête, vous avez exporté ce nouveau tableau en CSV et l'avez ré-importé en SQL ici même dans la table nommée "isf_population" qui vous est proposée ici.A l'aide de cette nouvelle table,  Proposez maintenant un classement des 20 villes ayant le pourcentage de redevables à l'ISF le plus élevé. 
**Indice 1**: pour calculer le pourcentage faites:
```
(isf_france.nb_redevables*100.0 / population.population)
```
**Indice 2** : utiliser un alias à ce calcul pour ordonner les résultats selon cette nouvelle variable ainsi créée

## 26
**Comparaison des 3 dimensions : Isf, Idh et population**
A l'aide de cette nouvelle table "isf_population", faites une fusion avec la table "idh_npdc" et ordonnez les villes avec le même calcul (adapté à la requête de fusion) de pourcentage de redevables à l'ISF. 
