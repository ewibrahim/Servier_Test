
# Test technique Servier

Projet de data engineering consistant à réaliser une data pipeline qui doit produire en sortie un fichier JSON qui représente un graphe de liaison entre les différents médicaments et leurs mentions respectives dans les différentes publications PubMed, les différentes publications scientifiques et enfin les journaux avec la date associée à chacune de ces mentions.
## 1. Preparation des données (```Functions/preprocessing/datapreprocessing.py```)

Application d'une série de traitement sur tous tous les fichiers se trouvant dans ```Data/Files``` vérifiant la qualité des données (dataframe vides, doublons, les nulls) et de nettoyage des données (suppression des charactères spéciaux, uniformisation des dates, conversion de types)

## 2. Transformation des données (```Functions/transformation/datatransformation.py```)

Transformation des données obtenues pour manipuler et traiter les données et sortir une réponse à la problématique posée.

## 3. Restitution des données (```Functions/postprocessing/datapostprocessing.py```)

Restitution des données en enregistrant différents dataframes en créant un fichier JSON qui représente un graphe de liaison entre les différents médicaments et leurs mentions respectives dans les différentes publications PubMed, les différentes publications scientifiques et enfin les journaux avec la date associée à chacune de ces mentions.

## 4. Réponses aux questions (6. Pour aller plus loin)

### 1. Faire évoluer le code

Pour ce projet, la librairie pandas a été utilisée mais pour faire évoluer le code afin qu'il puisse gérer de grosses volumétries de données, il faut considérer l'utilisation d'un système de traitement distribué de gros volumes de données tel que Spark qui est très efficace dans ce genre de contexte

### 2. SQL

#### Première partie du test:

Requête permettant de trouver le chiffre d’affaires (le montant total des ventes), jour par jour, du 1er janvier 2019 au 31 décembre 2019.

```SQL
WITH DATES(date)
AS
(
    SELECT '2019-01-01' as day
    UNION ALL
    SELECT day + 1
    FROM DATES
	WHERE day < '2019-12-31'
)
SELECT d.date, sum(t.prod_price*t.prod_qty) as ventes from dates d
JOIN TRANSACTION t on d.date = t.date
GROUP BY d.date
ORDER BY d.date ASC;
```

#### Deuxième partie du test:

Requête permettant de déterminer, par client et sur la période allant du 1er janvier 2019 au 31 décembre 2019, les ventes meuble et déco réalisées.

```SQL
SELECT  t.client_id,
CASE WHEN nomen.product_type="MEUBLE" THEN (TR.prod_price* TR.prod_qty) END as ventes_meuble,
CASE WHEN nomen.product_type="DECO" THEN (TR.prod_price* TR.prod_qty) END as ventes_deco
FROM TRANSACTIONS T
JOIN PRODUCT_NOMENCLATURE nomen ON t.prop_id=nomen.product_id
WHERE t.date  BETWEEN  "2019-01-01"  AND  "2019-12-31"
```