## 2. Codi font
  - Per crear un programa el que es farà serà crear un arxiu i escriure a un fitxer el
    seguit d’instruccions que es vol que l’ordinador executi.
  - Aquest arxiu és anomenat **codi font**:
  - El procés anomenat compilació és la traducció del codi font dels fitxers del
    programa en fitxers en format binari que contenen les instruccions en un format que el processador pot entendre. El contingut    d’aquests fitxers s’anomena **codi objecte**.
  - El **codi objecte** és el codi font traduït (pel compilador) a **codi màquina**, però aquest codi encara no pot ser executat     per l’ordinador.
  - El **codi executable** és la traducció completa a **codi màquina**, duta a terme per
    l’enllaçador (en anglès, _linker_). El codi executable és interpretat directament
    per l’ordinador.
  - L’ **enllaçador** és l’encarregat d’inserir al codi objecte les funcions de les **llibreries**
    que són necessàries per al programa i de dur a terme el procés de muntatge generant un arxiu executable.
  - Una **llibreria** és un col·lecció de codi predefinit que facilita la tasca del programador
    a l’hora de codificar un programa.
  - El concepte de màquina virtual sorgeix amb l’objectiu de facilitar el desenvolupament
    de compiladors que generen codi per a diferents processadors.
    La compilació consta de dues fases:
     - La primera parteix del codi font a un llenguatge intermedi obtenint un
       programa equivalent amb un menor nivell d’abstracció que l’original i que
       no pot ser directament executat.
     - La segona fase tradueix el llenguatge intermedi a un llenguatge comprensible
       per la màquina.
  - El gran avantatge de la JVM és que possibilita la portabilitat de l’aplicació a
    diferents plataformes i, així, un programa Java escrit en un sistema operatiu
    Windows es pot executar en altres sistemes operatius
