import random

#Aides : https://stackoverflow.com/questions/29938804/generate-random-sentences-in-python

#Génération aléatoire d'une Phrase en Anglais --DEBUT--
nouns = ["puppy", "car", "rabbit", "girl", "monkey","OtonaJP","A dude", "My mom", "The king", "Some guy", "A cat with rabies", "A sloth", "Your homie", "This cool guy my gardener met yesterday", "Superman","These dudes", "Both of my moms", "All the kings of the world", "Some guys", "All of a cattery's cats", "The multitude of sloths living under your bed", "Your homies", "Like, these, like, all these people", "Supermen"]                            #Liste de Noms utilisables
verbs = ["runs", "hits", "jumps", "drives", "barfs","eats", "kicks", "gives", "treats", "meets with", "creates", "hacks", "configures", "spies on", "retards", "meows on", "flees from", "tries to automate", "explodes"]                                                                                                                                                                                                                                           #Liste de Verbes utilisable
adv = ["crazily", "dutifully", "foolishly", "merrily", "occasionally","eventually","exactly","faithfully","finally","fortunately","frequently","gleefully","gracefully","happily","hastily","honestly","hopelessly","hourly","hungrily","innocently","inquisitively","irritably","jealously"]                                                                                                                                                                       #Liste d'adverbes utilisables 
adj = ["adorable", "clueless", "dirty", "odd", "stupid","quizzical","highfalutin","dynamic","wakeful","cheerful","thoughtful","cooperative","questionable","abundantuneven","yummy","juicy"]                                                                                                                                                                                                                                                                        #Liste d'adjectifs utilisables

random.shuffle(nouns)       #Mélange des éléments qui sont dans la liste des Noms
random.shuffle(verbs)       #Mélange des éléments qui sont dans la liste des Verbes
random.shuffle(adv)         #Mélange des éléments qui sont dans la liste des Adverbes
random.shuffle(adj)         #Mélange des éléments qui sont dans la liste des Adjectifs

num = random.randrange(0,13)                                                     #Méthode permettant la génération de la phrase aléatoirement et la stock dans une variable 'num'
phrase = nouns[num] + ' ' + verbs[num] + ' ' + adv[num] + ' ' + adj[num]
print (nouns[num] + ' ' + verbs[num] + ' ' + adv[num] + ' ' + adj[num])         #Affichage de la Phrase générer aléatoirement
print(phrase)
#Génération aléatoire d'une Phrase en Anglais --FIN--
