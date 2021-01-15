![workflow](https://user-images.githubusercontent.com/50483699/104626604-684ea600-5696-11eb-903c-a65fbc78f181.png)

Analyse de la degradation de celulles
========================================================
Le but est d'appliquer l'analyse fonctionnelle pour la prédiction
de performances de la cellules cyclée. Pour cela, on définit la dégradation
comme critère de performance, étant la perte d'energie moyenne d'un cycle à un autres.

\item[$\bullet$] L'étude doit montrer qu'une analyse univariée sur les premiers cycles
n'est pas suffisante pour pouvoir analyser la dégradation de la batterie.
  - il suffit de montrer que la correlation entre la dégradation sur les premiers cycles
et celle totale n'est pas suffisamment forte.
  - la visualisation des courbes SoH en fonction de la dégradation totale n'est pas un critère
suffisant pour un expérimentateur pour conclure sur la qualité de la cellule.



$\bullet$ Pour contrer cela, une analyse fonctionnelle sur des données issues
des premiers cycles sera appliquée. C'est à dire, une regression logistique fonctionnelle et une regression pénalisée
focntionnelle sont mis en places pour prédire respectivement :

- au moment du cycle 30, la qualité finale de dégradation de la celulle sur l'ensemble 
  de son cyclage.
- au moment du cycle 100, la valeur exacte de dégradation.


 
 Auteurs
 ========================================================
  - **Marc Duquesnoy** , PhD (@MarcDuquesnoy), marc.duquesnoy@u-picardie.fr
  
 Contributeurs
========================================================
  - **Marc Duquesnoy** , PhD (@MarcDuquesnoy), marc.duquesnoy@u-picardie.fr

 
 Licence
========================================================

Ce répertoire est sous licence [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) licence.