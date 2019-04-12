Il s'agit d'un jeu type shoot-them-up à la verticale. Un star field descendant est visible en fond durant toute la durée du jeu (même sur l'écran de démarrage). Une petite boucle sonore tourne en permanence.

Le but est de faire le plus haut score avec une unique vie.

# Écran de démarrage

* Lorsque le jeu démarre les inscriptions suivantes sont visibles : 
  * Titre du jeu
  * par Théo
  * Hi-score : 00000
  * Touches flèches : déplacement
  * X : tir
  * Presser X pour démarrer
* Le nombre derrière hi-score sera remplacé par le score le plus élevé jamais réalisé.

# Player

* Le joueur manipule un vaisseau . Déplacement orthogonaux uniquement (pas de diagonales) grâce aux touches 'flèches' du clavier. 
* La touche 'x' permet de tirer.  Le vaisseau tir une onde laser aussi large que le vaisseau.  Un son spécifique est émis à ce moment. Maintenir la touche 'x' enfoncée permet de tirer en continue. (fréquence max. 8 tirs/seconde)
* Le joueur  meurt si il est touché par un ennemi ou un tir d'ennemi
* Lorsque le joueur meurt une explosion est visible à l'emplacement de la collision. Une pause deux secondes est aménagée avant de revenir à l'écran de démarrage, durant laquelle toutes les entités présentes à l'écran poursuivent leur trajectoire.
* Le joueur ne peut pas sortir de l'écran. Il reste bloquer en limite même si les touches de directions sont enfoncées.

# Ennemis

Il y 3 sortes d'ennemis + 1 boss. Les ennemis descendant du haut vers le bas. Tous les ennemis sont représentés clignotant sur deux frames alternant tout les secondes.

Dés qu'un ennemi est tué tout l'écran flash de la couleur dominante propre à chaque ennemi sur une frame. Une explosion ( de particules) d'une durée d'une seconde démarre à ce instant.  Un son spécifique est émis.

## Tirs ennemis

* Les tirs des ennemis sont représentée par une petite boule d'énergie (une frame).
* Les boules se déplacent en ligne droite
* La trajectoire de la boule suit une ligne droite entre le centre du l'ennemi et le centre du joueur déterminée au moment du début du tir. 
* Si la boule entre en collision avec le joueur elle explose puis disparait
* La boule est détruite après sa sortie d'écran

## Ennemi 1

* Il meurt si il est touché par un tir du joueur
* Il tire une boule toutes les 2 secondes

## Ennemi 2

* Il est constitué de 7 segments qui se suivent sur sa trajectoire de déplacement
* Chaque segment est autonome et peut être détruit par un tir du joueur
* Si un segment meurt les autres ne sont pas affectés et poursuivent leur trajectoire.
* Cet ennemi ne tire pas

## Ennemi 3

* Cet ennemi tire une bullet toutes les deux secondes.
* Il faut trois tirs pour tuer cet ennemi.

## Déplacements

Chaque ennemi suit une logique de déplacement spécifique.

![shooter_dep.png](https://files.nuclino.com/files/2f2cd419-1532-4201-9c00-ff86c88cce3b/shooter_dep.png)

## Le boss

### Déplacement

* en x : il commence au centre ( voir schéma. pos 1) puis se déplace vers la droite (pos2). Revient au centre (pos1) puis va vers la gauche (pos3). Le boss revient au centre pos1 recommençant ainsi le cycle en enchaînant vers la droite (pos 2). À chaque position une pause d'une seconde est effectué et il effectue les transition entre chaque pause en 2 secondes.
* en y : il démarre hors écran (pos 0 ) et descend au centre de l'écran en 6 secondes. Une fois le centre atteint il y reste jusqu'à ce que le joueur ou lui même meurt.
* Les deux mouvements décrit ci dessus sont simultanés.

![shooter_boss.png](https://files.nuclino.com/files/054ad22f-366b-44d1-9593-550b26ecef78/shooter_boss.png)

### Tir

* Le boss tire des salves de 16 bullets qui partent de son centre. 
* Les 16 bullets sont réparties uniformément sur un cercle et suivent une trajectoires rectilignes.
* Le boss tire une salve à chaque seconde. Un son spécifique est émis.

### Condition de victoire

* Une barre de vie est affichée au centre et vers le haut de l'écran représentant la vie du boss. 
* L'intérieur de cette barre diminuera proportionnellement à la vie restante du boss.
* Il faut tirer 100 fois sur le boss pour l'anéantir.
* A chaque fois que le boss est touché par un tir, celui-ci flash d'un couleur différente et sa position en y est légèrement remonté ( pour montrer l'impact qui le touche et le pousse vers le haut.)  Plusieurs tire consécutifs touchant le boss cumule le décalage vers le haut. Ce décalage toute fois n'ira jamais au delà d'un certain seuil juste en dessous de la barre de vie. Quoiqu'il arrive le boss redescend progressivement et cherche à reprendre sa place centrale en verticalité.
* Losrque le boss meurt une giga explosion est représentée ( plusieurs mini explosion de particule comme un feu d'artifice). Un son accompagne l'explosion.

# Vagues d'ennemis

* Une vague d'ennemi est un assemblage de plusieurs ennemis de type différents dont la position de départ et le timing de départ sont pré-déterminés.
* Le timing de départ sert à décaler l'apparition des ennemis dans le temps pour qu'il n'apparaissent pas tous simultanément. Toutefois un ennemi peut être spawné alors que d'autres sont encore présents à l'écran.
* Une ennemi démarre toujours en haut et hors écran et évolue vers le bas.
* Chaque nouvelle vague augment en difficulté ( nombre d'ennemis et stratégie de position différentes )
* 7 vagues sont prévues avant l'apparitIon du boss.
* Avant l'apparition du boss la boucle sonore change (éventuellement les couleurs de fond change mais c'est pas obligatoire)
* Si le boss est vaincu, une dernière vague (courte et facile) est prévue pour laisser souffler le joueur avant de recycler sur la première. 