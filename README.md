# Dechifrement_Porta

Ce Code sert  à cryptanalyser le chiffre de PORTA , en Utilisant la méthode de recherche par mot probable.
# Input  
- l'utilisateur saisie leur message crypter et le mot probable qui peut  apparaitre dans le message clair

# Output

- le Cle et les message clair 


# Idée Générale  

- L'idée est d'utiliser la faille de sécurité  : l'image chifrée d'une  lettre qui appartient à la 1ere moitié de l'alphabet  , appartient  à la deuxième moitié de l'alphabet et vice versa 


# Methode de travail 
Mon algorithme implemente tout d'abord  le tableau de porta sous la forme des Listes de tuple qui contient chaqu'une un couple d'alphabet . Aprés , un dictionnaire relie les listes de tuple avec les Alphabet de porta . Ensuite  , je transforme le chifre de porta et le mot probable ,saisie ,  en une liste de nombre (ensemble de deux et un )   , ainsi  ,je fait une recherche sur le complément du  mot probable dans le liste du nombre duchifre de porta .Ensuite , je relie les deux couple mot probable et portion du chifre correspondante avec l'alphabet de porta . Entrouve ceci le cle. Enfin , grace à ce cle on fait le décryptage du hash    

#Execution 

python Hacking_Porta.py 
