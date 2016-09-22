# Enoncé

Récupérez le fichier "exam_DB.sqlite" et chargez le dans SQLiteMan. Vous verrez les 4 tables utilisées dans cet examen.
Reprenez l'énoncé de l'examen dans un éditeur de texte de votre choix, et recopiez les requêtes SQL permettant de répondre à la question, sous chacune des questions. 
Remettez ensuite ce fichier dans le devoir "Examen de fin de semestre" sur le site Moodle du cours:
http://moodle.univ-lille3.fr/course/view.php?id=4904

Si vous rencontrez des difficultés, envoyez le fichier réponse par email `freddy.limpens@univ-lille3.fr`

# Présentation des tables

## 1 "isf_france"
Base de données ISF (Impôt de Solidarité sur la Fortune)
- Pour l'ANNEE 2009
- pour les Villes de plus de 20 000 habitants ayant plus de 50 redevables à l'ISF

## 2 "idh_npdc" 
Indice de Développement Humain calculé (année 2009) pour les communes de la région Nord - Pas de Calais

## 3 "population"
Population des communes de France de plus de 20 000 habitants (2009)

## 4 Fusion des tables "population" et "isf_france"
Avec les champs:
- commune 
- nb_redevables
- population

# 1. Exercices sur la table "isf_france"
 
## 1
Donner le nombre de communes concernées par cette table

```sql
  SELECT COUNT(*) FROM isf_france
```

## 2
Donner la liste des communes ayant un nombre de contribuables ISF supérieur à 1000 personnes

```sql
SELECT * from isf_france
WHERE nb_redevables > 1000
```
## 3
Donner la liste des communes, et la patrimoine moyen des contribuables à l'ISF dont le patrimoine moyen est supérieur à 2,000,000 €?
```sql
SELECT commune, patrimoine_moyen FROM isf_france
WHERE patrimoine_moyen > 2000000 
```
## 4
Donner la liste des communes dont le nombre de redevables est inférieur à 1000 et le patrimoine moyen supérieur à 2500000€?
```sql
SELECT * from isf_france
WHERE nb_redevables < 1000 AND patrimoine_moyen > 2500000
```
## 5
Même question, mais en classant les villes par patrimoine moyen en ordre décroissant
```sql
SELECT commune, patrimoine_moyen FROM isf_france
WHERE patrimoine_moyen > 2000000
ORDER BY patrimoine_moyen DESC
```
## 6
le mot clé LIMIT ajouté à la fin d'une requête permet de limiter le nombre de résultat. 
En ajoutant par exemple LIMIT 10 aux requêtes précédentes, vous limiterez le nombre de communes résultantes à 10 
 Fort de cette nouvelle connaissance, donner la liste des 20 communes les plus "riches", c'est à dire avec les patrimoines moyens les plus élevés.
 ```sql
SELECT commune, patrimoine_moyen FROM isf_france
ORDER BY patrimoine_moyen DESIC
LIMIT 20
```
## 7
Même question, mais en excluant la ville de PARIS
```sql
SELECT commune, patrimoine_moyen FROM isf_france
WHERE commune IS NOT 'PARIS'
ORDER BY patrimoine_moyen DESC
LIMIT 20
```
## 8
Donner le nombre de villes comprenant des redevables à l'ISF dans le département du NORD; 
```sql
select * from isf_france
where departement = 'NORD'
```

## 9
Idem, mais dans le département du PAS DE CALAIS; 
```sql
select * from isf_france
where departement = 'PAS-DE-CALAIS'
```
## 10
Effacer de cette table les valeurs pour la région "Centre"
```sql
DELETE FROM isf_france
where region = 'CENTRE'
```
## 11
Proposer une requête pour vérifier que les valeurs ont bien été effacées 
```sql
SELECT * from isf_france
where region = 'CENTRE'
```

# Table Indice de développement humain "idh_npdc"

## 12
 Donner les 30 premières villes classées par idh du plus au moins élevé
 ```sql
SELECT * from idh_npdc
order by idh desc 
```
## 13
Donner l'idh et le nom de commune pour les villes suivantes: Lille, Tourcoing, Roubaix, Croix, La Madeleine
```sql
SELECT * from idh_npdc
where nom_commune in ('LILLE', 'TOURCOING', 'ROUBAIX', 'CROIX', 'LA MADELEINE')
```
## 14
créez une table nommée mon_idh et contenant 2 colonnes, une pour le nom des communes, l'autre pour la valeur de l'idh (nombre à virgule)

## 15
Insérez dans cette table les valeurs relevées ci-dessus pour les villes de Lille, Tourcoing, Roubaix, Croix, La Madeleine

## 16
Donner les villes qui ont un idh supérieur à 0.750
```sql
SELECT * from idh_npdc
where idh > 0.76 
```

## 17
Parmis ces villes, combien sont situées dnas le département du Nord ? Indice: vous pouvez soit considérer le code postal comme un nombre (compris entre 59000 et 59999) ou une chaine de charactère commençant par '59'.
```sql
SELECT * from idh_npdc
where idh > 0.76 AND code_postal LIKE '59%'
```

## 18
Combien dans le département du Pas de Calais 
```sql
SELECT * from idh_npdc
where idh > 0.76 AND code_postal > 62000
```

# Table population

# 19
Donner le nom de commune, la population pour les villes de plus de 20 000 habitants du Nord et du Pas de Calais. Ordonnez par nombre d'habitants, dans l'ordre décroissant
```sql
SELECT commune, population
FROM population
where dept = 59 OR dept = 62
ORDER BY population DESC
```
## 20
Combien y'a t-il de ville de plus de 100 000 habitants en France ?
```sql
SELECT COUNT(*)
from population
WHERE population > 100000 
```

## 21
Combien de villes de plus de 100 000 habitants dans la région Nord - PAs de Calais ?
```sql
SELECT COUNT(*)
from population
WHERE population > 100000 AND (dept = 59 OR dept = 62)
```

# Fusions

## 22
Proposez une fusion entre la table Indice de développement humain "idh_npdc" et la table "population"
```sql
SELECT * 
from idh_npdc
inner join population
on population.commune LIKE idh_npdc.nom_commune
```
## 23
Sur la base de cette fusion, proposer un classement des villes du Nord Pas de Calais de plus de 30000 habitants, classées apr idh descendant (indice: écrivez les contraintes de filtrage et d'ordre *après* les règles de fusion)
```sql
SELECT * 
from idh_npdc
inner join population
on population.commune LIKE idh_npdc.nom_commune
where population.population > 30000
ORDER BY idh_npdc.idh DESC
```

# 24
Proposer une requête pour faire la fusion entre la table "isf_france" et la table "population". L'objectif de cette fusion est d'obtenir une table comportant les colonnes suivantes:
- nom de la commune
- nombre de redevables à l'ISF
- population de la commune  
```sql
SELECT population.commune, isf_france.nb_redevables, population.population
FROM isf_france 
INNER JOIN population
ON isf_france.commune LIKE population.commune
```

## 25
Suite à cette requête, vous avez exporté ce nouveau tableau en CSV et l'avez ré-importé en SQL ici même dans la table nommée "isf_population" qui vous est proposée ici.A l'aide de cette nouvelle table,  Proposez maintenant un classement des 20 villes ayant le pourcentage de redevables à l'ISF le plus élevé. 
**Indice 1**: pour calculer le pourcentage faites:
```
(isf_france.nb_redevables*100.0 / population.population)
```
**Indice 2** : utiliser un alias à ce calcul pour ordonner les résultats selon cette nouvelle variable ainsi créée

```sql
SELECT commune,  (nb_redevables*100.0 / population) AS percent
FROM isf_population
ORDER BY percent DESC
```
 
## 26
**Comparaison des 3 dimensions : Isf, Idh et population**
A l'aide de cette nouvelle table "isf_population", faites une fusion avec la table "idh_npdc" et ordonnez les villes avec le même calcul (adapté à la requête de fusion) de pourcentage de redevables à l'ISF. 
```sql 
SELECT idh_npdc.idh, isf_population.commune, (isf_population.nb_redevables*100.0/isf_population.population) AS percent
from idh_npdc
inner join isf_population
on idh_npdc.nom_commune LIKE isf_population.commune
ORDER BY percent DESC
```