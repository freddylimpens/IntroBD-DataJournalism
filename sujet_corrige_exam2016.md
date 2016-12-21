# Enoncé

```sql(.*\n)+?```

Récupérez le fichier "exam2016.db.sqlite" et chargez le dans SQLiteMan. Vous verrez les 4 tables utilisées dans cet examen.
Reprenez l'énoncé de l'examen dans un éditeur de texte de votre choix, et recopiez les requêtes SQL permettant de répondre à la question, sous chacune des questions.
Remettez ensuite ce fichier dans le devoir "Examen de fin de semestre" sur le site Moodle du cours:
http://moodle.univ-lille3.fr/course/view.php?id=4904

Si vous rencontrez des difficultés, envoyez le fichier réponse par email `freddy.limpens@univ-lille3.fr`


# Surface bio et SAU (Surface Agricole Utile) des départements français

La table `surf_bio_evol` donne l'identifiant et le nom de département (numéro), la surface bio, et la SAU (Surface Agricole Utile) des départements français pour les années 2001 et 2012

## Question
Donnez le nom de département, la SAU 2001, et la SAU 2012 des départements de la région Hauts de France, ordonnée par SAU de 2001 descendante

```sql
select nom_departement, sau_2001, sau_2012 from surf_bio_evol
where id_departement in (59,62,80,02,60)
order by sau_2001 desc
```

## Question
Toujours pour les départements des Hauts de France, affichez le nom et la différence entre la SAU 2012 et la SAU 2001 (2001 - 2012), ordonnez les départements par ordre de différence décroissante (de celui qui a perdu le plus vers celui qui a perdu le moins)

```sql
select nom_departement, (sau_2001-sau_2012) as diff from surf_bio_evol
where id_departement in (59,62,80,02,60)
order by abs(diff) desc
```

## Question
Y'a t'il des départements, au niveau de la France entière à présent, dont la SAU a augmenté entre 2001 et 2012 ? Donnez leur liste et la différence de SAU.
```sql
select nom_departement, (sau_2001-sau_2012) as diff from surf_bio_evol
where diff < 0
```

## Question
Y'a t'il des départements dont la surface bio en 2012 est nulle ? Donnez leur liste.
```sql
select nom_departement from surf_bio_evol
where surf_bio_2012 is null
```

## Question
Donnez la liste des départements dont la surface bio est comprise entre 20000 et 50000 ha. Ordonnez par surface décroissante.
```sql
select nom_departement, surf_bio_2012 from surf_bio_evol
where surf_bio_2012 > 20000 and surf_bio_2012 < 50000
order by surf_bio_2012 desc
```

## Question
Y'a t'il des départements dont la surface bio a baissé entre 2001 et 2012 ? Donnez une requête permettant de le vérifier.
```sql
select nom_departement, surf_bio_2012 from surf_bio_evol
where surf_bio_2012 < surf_bio_2001
```

<!--
Le bio dans les Hauts de France. Donnez le nom et leur surface bio pour les départements des Hauts de France, et classez les par surface bio décroissante.
```sql
select nom_departement,  surf_bio_2012 from surf_bio_evol
where id_departement in (59,60,80,62,02)
order by surf_bio_2012 desc
``` -->

## Question
Dans les Hauts de France, classez maintenant les départements en fonction de leur pourcentage de surface bio par rapport à leur SAU, par ordre décroissant de ce pourcentage (que vous afficherez également)
```sql
(formule : surface bio x 100 / SAU)

select nom_departement,  surf_bio_2012*100/sau_2012 as percent from surf_bio_evol
where id_departement in (59,60,80,62,02)
order by percent desc
```

## Question
Donnez le nom et le pourcentage de surface bio par rapport à la SAU, pour tous les départements de France en excluant seulement le département des HAUTS-DE-SEINE. Ordonnez toujours par pourcentage décroissant.
```sql
select nom_departement,  surf_bio_2012*100/sau_2012 as percent from surf_bio_evol
where nom_departement != 'HAUTS-DE-SEINE'
order by surf_bio_2012*100/sau_2012 desc
```

# Population des départements français

La table `population_dpt` donne le nom de région, l'identifiant et le nom, le nombre de communes et la population pour les départements français.

## Question
Donnez le nom de département, le nombre de commune, et la population des départements appartenant à présent à la région Hauts de France (aidez vous de wikipedia au besoin)
```sql
select nom_departement, nb_communes, population from population_dpt
where region in ('PICARDIE', 'NORD-PAS-DE-CALAIS')
```

## Question
Donnez le nom de département, le nombre de commune, et la population des départements dont le nom de région commence par la lettre 'P' ou par la lettre 'N'
```sql
select nom_departement, nb_communes, population from population_dpt
where region LIKE 'P%' or region LIKE 'N%'
```


## Question
En utilisant une fusion avec la table `surf_bio_evol`, donnez pour chaque département : son nom, et le nombre d'hectare de SAU pour 10 habitants. Ordonnez selon cette valeur de manière décroissante.
```sql
select surf_bio_evol.nom_departement, (10*sau_2012)/population_dpt.population as sau_par_hab
from surf_bio_evol join population_dpt
on population_dpt.id_departement = surf_bio_evol.id_departement
order by sau_par_hab desc
```


# Surface et Nombre d'exploitants bio des départements français

Voir le tableau `exp_surf_bio_2012` mettant en lien nombre d'exploitant bio et surface bio par département pour l'année 2012

## Question
Donnez l'id du département et le nombre d'exploitants bio, classés par ordre décroissant, et pour les 10 premiers départements

```sql
select id_departement, nb_exp_bio
from exp_surf_bio_2012
order by  nb_exp_bio desc
limit 10
```


## Question
Donnez l'id du département et la surface moyenne par exploitation pour chaque département. Ordonnez les départements par surface moyenne décroissante, et n'affichez que les 10 premiers.

```sql
select id_departement, surf_bio/nb_exp_bio as surf_moy
from exp_surf_bio_2012
order by  surf_moy desc
limit 10
```

## Question
Refaites le même calcul, mais en affichant le nom du département au lieu de son identifiant en effectuant une fusion avec la table `population_dpt`
```sql
select  population_dpt.nom_departement, exp_surf_bio_2012.surf_bio/exp_surf_bio_2012.nb_exp_bio as surf_moy
from exp_surf_bio_2012
join population_dpt
on exp_surf_bio_2012.id_departement = population_dpt.id_departement
order by  surf_moy desc
```

## Question
En fusionnant les mêmes tables `population_dpt` et `exp_surf_bio_2012`, donnez maintenant le nom de département et le nombre d'exploitants bio pour 10 000 habitants pour chaque département ; ordonner selon cette valeur par ordre décroissant.

```sql
(formule : nombre exploitant x 10000 / population du département)

select  population_dpt.nom_departement, exp_surf_bio_2012.nb_exp_bio*10000/population_dpt.population as exp_pour_10000
from exp_surf_bio_2012 join population_dpt
on exp_surf_bio_2012.id_departement = population_dpt.id_departement
order by  exp_pour_10000 desc
```

# Table `distributeurs`
Cette table donne le nombre de distributeurs bio par département en 2011 (pour les comparaisons avec les autres tables on supposera que ce nombre a faiblement évolué en 2012).

## Question
Calculez la valeur moyenne du nombre de distributeurs arondie à l'entier (sans décimale)
```sql
select round(avg(nb_distributeur),0) from distributeurs
```

## Question
Créez une table appelée `resultats` comprenant 2 colonnes: 1 appelé `variable`, contenant du texte, l'autre appelé `valeur` et contenant un nombre entier.


## Question
Insérez dans cette table nouvellement créée la valeur calculée précédemment en lui donnant le nom de votre choix (si vous n'avez pas réussi à la calculer, donnez une valeur arbitraire).



## Question
Donnez une requête permettant de compter les départements dont le nombre de distributeurs est supérieur à la moyenne précédemment calculée (utilisez une valeur arbitraire sinon)
```sql
select count(departement) from distributeurs
where nb_distributeur > 33
```

## Question
Donnez le nom de département, et le nombre de distributeurs pour les départements de la nouvelle région Haut de France qui comptent plus de distributeurs que le moyenne précédemment calculée.
```sql
select departement, nb_distributeur from distributeurs
where nb_distributeur > 33 and region in ('PICARDIE', 'NORD-PAS-DE-CALAIS')
```


## Question
Donnez le nom de région, et la somme des distributeurs pour chaque région, ordonnez les régions par nombre décroissant de distributeurs bio

```sql
select region, sum(nb_distributeur) as sum from distributeurs
group by region
order by sum desc
```

## Question
A l'aide d'une fusion avec la table `exp_surf_bio_2012`, donnez le nom de département et le nombre de producteur par distributeurs (ratio) pour chaque département. Ordonnez les valeurs par ordre décroissant de ce ratio.
```sql
select distributeurs.departement, exp_surf_bio_2012.nb_exp_bio/distributeurs.nb_distributeur as ratio,
from distributeurs
join exp_surf_bio_2012
on distributeurs.id_departement = exp_surf_bio_2012.id_departement
order by ratio desc
```

## Question
A l'aide d'une fusion avec la table `population_dpt`, afficher maintenant pour tous les départements leur nom et le ratio de nombre de distributeurs pour 100 000 habitants
```sql
select distributeurs.departement, distributeurs.nb_distributeur*100000/population_dpt.population as ratio
from distributeurs join population_dpt
on  population_dpt.id_departement = distributeurs.id_departement
order by ratio desc
```
