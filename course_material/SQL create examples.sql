-- Création d'une table
-- format à suivre :
CREATE TABLE table_name
(
column_name1 data_type(size) constraint_name,
column_name2 data_type(size) constraint_name,
column_name3 data_type(size) constraint_name,
....
);

-- exemple :

CREATE TABLE etudiants_bd (
  id int,
  nom varchar(255),
  prenom varchar(255),
  email varchar(255)
);

-- insertion de valeurs
INSERT INTO etudiants_bd 
VALUES (1, 'bergson', 'henry', 'bergsonh@no-log.org')

INSERT INTO etudiants_bd (nom, email)
VALUES ('sartre', 'jps@gmail.com')

-- Mise à jour des valeurs d'une ou plusieurs lignes
UPDATE etudiants_bd
SET id=2, prenom= 'jean paul'
WHERE nom LIKE 'sartre'
