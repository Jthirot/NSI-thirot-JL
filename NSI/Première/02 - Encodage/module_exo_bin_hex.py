def no_zero(s) :
    i=0
    while s[i]=="0" :
        i+=1
    return s[i:]

def check(ex,q,reponse) :
    if ex==1 :
        if q==1 : ans=2
        if q==2 : ans=9
        if q==3 : ans=13
        if q==4 : ans=25
        if q==5 : ans=31
    if ex==2 :
        if q==1: ans = "1011"
        if q==2: ans = "10110"
    if ex==3 : 
        reponse = reponse[reponse.index("1"):]
        if q==1 : ans="100"
        if q==2 : ans="111"
    if ex==4 : 
        reponse = reponse[reponse.index("1"):]
        if q==1 : ans="1101010"
    if ex==5 : 
        if q==1 : ans=2
        if q==2 : ans=4
        if q==3 : 
            ans=255
            if reponse == 256 : print("On commence à 0, ta réponse est proche mais pas tout à fait exacte...")
        if q==4 : ans=65535
        if q==5 : ans=9
        if q==6 : ans=125
        if q==7 : ans=8000
    if ex == 7 :
        an1,an2 = reponse
        ans = (256,57181)
        if an1 == 256 : 
            print("oui, il est possible de coder 256 couleurs, cette réponse est correcte")
        elif an1 == 255 :
            print("nb-de_couleurs : tu as répondu 255. Ici on ne demande pas le plus grand entier, mais combien de couleurs...")
        else :
            print("nb-de_couleurs : tu as répondu ",an1," cette réponse n'est pas correcte.")
        if an2 == 57181 : 
            print("oui, l'image requière 57181 octets, cette réponse est juste")
        elif an2 == 57181*8 : 
            print("tu as calculé le nombre de bits, on demande en octets")
        else :
            print("no_octets: tu as répondu",an2,"cette réponse n'est pas correcte.")
    if ex == 8 :
        if type(reponse) != str : 
            print("La réponse attendu est une chaine de caractère....")
        else :
            reponse = reponse[reponse.index("1"):]
        if q == 1 : ans = "101"
        if q == 2 : ans = "1010"
        if q == 3 : ans = "10000000"
        if q == 4 : ans = "111111"
        if q == 5 : ans = "1111101000"

    if ex == 9 :
        if q==1 : ans = 10
        if q==2 : ans = 11
        if q==3 : ans = 20
        
    if ex == 11 :
        if q==1 : ans = 16
        if q==2 : ans = 42
        if q==3 : ans = 255

        
    if ex == 12 :
        if q==1 : ans = "11000011"
        if q==2 : ans = "110000001010"
        if q==3 : ans = 255    

    if ex == 13 :
        if q==1 : ans = "D6"
        if q==2 : ans = "B0"
        if q==3 : ans = "144"    

    if ex == 14 :
        reponse = no_zero(reponse)
        if q==1 : ans = "A"
        if q==2 : ans = "44"

    if ex==16 :
        n,bleu,blanc,noir = reponse
        ans = (255**3,"#0000ff","#ffffff", "#000000")
        reponse = (n,bleu.lower(),blanc.lower(),noir.lower())
        if n == 255**3 : 
            print("nombre de couleur :",n," - Bonne réponse")
        else :
            print("nombre de couleur :",n," - Mauvaise réponse")

        if bleu.lower() == "#0000ff" : 
            print("bleu :",bleu," - Bonne réponse")
        else :
            print("bleu :",bleu," - Mauvaise réponse")
        if blanc.lower() == "#ffffff" : 
            print("blanc :",blanc," - Bonne réponse")
        else :
            print("blanc :",blanc," - Mauvaise réponse")
        if noir.lower() == "#000000" : 
            print("noir :",noir," - Bonne réponse")
        else :
            print("noir :",noir," - Mauvaise réponse")

    if reponse == ans :
        print("bonne réponse")
    else :
        print("Tu as fait une erreur, essaye à nouveau")
        
def check_bin2dec(f) :
    assert f("10") == 2,"Tu as une erreur, l'appel bin2dec( \"10\") devrait renvoyer 2 et il renvoie "+str(nb_bits(5))
    assert f("111") == 7,"Tu as une erreur, l'appel bin2dec( \"111\") devrait renvoyer 7 et il renvoie "+str(bin2dec('111'))
    print("Tous les tests ont été réussis, ton code semble correct.")

def check_nb_bits(f) :
    assert f(0) == 1,"Tu as une erreur, l'appel nb_bits(0) devrait renvoyer 1 et il renvoie "+str(nb_bits(0))
    assert f(5) == 3,"Tu as une erreur, l'appel nb_bits(5) devrait renvoyer 3 et il renvoie "+str(nb_bits(5))
    assert f(10**6) == 20,"Tu as une erreur, l'appel nb_bits(10**6) devrait renvoyer 20 et il renvoie "+str(nb_bits(10**6))
    print("Tous les tests ont été réussis, ton code semble correct.")

def check_hexa2dec(f) :
    for h in ["0","10","100"] :
        ans = int(h,16)
        assert f(h) == ans,"Tu as une erreur, l'appel hexa2dec("+h+") devrait renvoyer "+str(ans)+" et il renvoie "+str(hexa2dec(h))
    print("Tous les tests ont été réussis, ton code semble correct.")

def check_dec2bin(f) :
    assert type(f(2))==str,"La fonction devrait renvoyer une chaine, elle renvoi :"+str(type(f(2)))
    assert f(2) == "10","Tu as une erreur, l'appel dec2bin(2) devrait renvoyer \"10\" et il renvoie \""+str(dec2bin(2))+"\""
    assert f(8) == "1000","Tu as une erreur, l'appel dec2bin(8) devrait renvoyer \"1000\" et il renvoie "+str(dec2bin(8))
    #assert f("111") == 7,"Tu as une erreur, l'appel bin2dec( \"111\") devrait renvoyer 7 et il renvoie "+str(bin2dec('111'))
    print("Tous les tests ont été réussis, ton code semble correct.")