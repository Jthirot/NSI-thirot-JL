def afficher(bonne,eleve) :
    if bonne == eleve : print("Bonne réponse")
    else :print("Mauvaise réponse")
def check_answer(num,rep) :
    if num == 1 : afficher("D",rep)
    if num == 2 : afficher("C",rep)
    if num == 3 : afficher("B",rep)
    if num == 4 : afficher("D",rep)
    if num == 5 : afficher("A",rep)
    if num == 6 : afficher("B",rep)
    if num == 7 : afficher("C",rep)
