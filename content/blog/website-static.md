Title: Site Web Statique
Date: 2015-06-20
Authors: ptanguy
slug: website-static
Summary: Retour d'expérience sur l'utilisation de générateur de site web statique en Python
Status: draft

Les sites web statiques redeviennent à la mode ces derniers temps.
Leurs constructions sont rendus plus faciles et agréables avec l'apparation de générateur de sites web statiques.
Jekyll (Ruby) associé à github pour la génération et l'hébergement des pages web à probablement participé à ce renouveau.
À titre d'exemple, le site [staticgen](https://www.staticgen.com) répertorie un nombre important de ces générateurs et cela dans plusieurs languages de programmation.
En ce qui me concerne, j'ai testé les générateurs écrits en Python suivant: Hyde, Pélican et Urubu. 
Suivant le générateur choisi, le cadriciel sera généralement plus ou moins orienté.
Par exemple, de mon point de vue Pélican est vraiment orienté pour l'écriture d'un blog alors que Urubu va permettre de générer un site web quelconque plus librement.
De même, d'autre comme Mkdocs ou Sphinx vont permettre d'écrire de la documentation en reStructuredText ou Markdown et la générer sous forme de page web Html. 


Le flux de travail développé autour d'un cadriciel générateur de page web peut être plus ou moins développé.
En effet, certain utilise des logiciels de gestions de versions comme git pour gérer leur site.
D'autres ajoutent aussi des méthodes d'intégration continu pour le déploiement de leurs pages web comme Travis CI par exemple.
