-- Création d'une table
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


