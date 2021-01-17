import random,time

with open("eminem_lyrics.txt", encoding="utf8") as f:
        lyrics = f.readlines()

alphabet = ["a","b","c","d","e","f","g","h","i","j","k",
            "l","m","n","o","p","q","r","s","t","u","w"
            ,"y"]

##############################################################################################################
#alkuosa
##############################################################################################################
first_letter = random.choice(alphabet).upper()
#Generoidaan rivin ensimmäinen sana, joka on myös sana, jolla Eminem on aloittanut rivin
def eka_sana(sana=first_letter):
    backup_sana = sana
    while True:
        try:
            test1 = []
            next_letters = []
            
            for i in range(len(lyrics)):
                if sana in lyrics[i]: #jos sana löytyy tarkastelussa olevalta riviltä:
                    if sana[0] == lyrics[i][0]: #jos sanan ensimmäinen kirjain matchaa rivin ekan kirjaimen kanssa:
                        for j in range(len(sana)):
                            test1.append(lyrics[i][j+1]) #lisätään väliaikaiseen listaan kirjaimet talteen
                            
                        next_letters.append(test1[-1]) #lisätään riveiltä kerätyistä sanoista seuraavat kirjaimet listaan, jota käytetään seuraavan kirjaimen ennustamiseen

            next_letter = random.choice(next_letters) #uusi kirjain valitaan randomilla kerätyistä vaihtoehdoista
            if next_letter == " ": #jos ehdotettu merkki on välimerkki, sana on valmis ja looppi voidaan lopettaa
                break
            else: #jos ehdotettu merkki on kirjain, lisätään se sanan jatkoksi
                sana += next_letter

        #hardcoded mut huomaamaton fixi dumbass erroriin
        except:
            #sanavalikko = ["You","I","And","No","To"]
            sana = backup_sana
    
    return sana   


#Etsitään rivi, joka alkaa rakentamallamme sanalla ja lisätään siitä 2 seuraavaa sanaan luodaksemme lauseenalun
def jatkoa_lauseelle(sana=eka_sana()):
    try:
        i_lista = []
        testi1 = []
        alku = []
        
        for i in range(len(lyrics)):
            if sana in lyrics[i]: #etsitään kaikki rivit, jotka alkavat sanallamme
                i_lista.append(i)

        i = random.choice(i_lista) #valitaan randomilla rivi
        aika = time.time()
        while lyrics[i].count(" ") < 3: #jos rivillä on alle 3 sanaa, arvotaan rivi uudestaan
            if time.time()-aika >= 0.2: #jos jäädään infinite looppiin, breakataan se
                break
            
            i = random.choice(i_lista)
            
        for j in range(len(lyrics[i])):
            if lyrics[i][j] == " ": #jos tulee space vastaan, niin kerätään talteen sen takana olevat sanat
                testi1.append(lyrics[i][:j])


        #testi1 sisältää pirusti kamaa mut sen kolmas arvo sisältää vain 3 ekaa sanaa joita me halutaan käyttää
        return testi1[2]

    #harvat tapaukset, joissa ei löydetä riittävän pitkää riviä ratkaistaan tällä
    except:
        try:
            return testi1[1]    
        except:
            return testi1[0]


alku1 = jatkoa_lauseelle()
def toka_rivi_alku(sana=alku1):
    testi1 = []
    alku = []
    
    #jos rivi, jossa on vain 3 sanaa, tulee valituksi, tulee error, koska testi1 sisältää vain 2 arvoa
    try:
        
        for i in range(len(lyrics)):
            if sana in lyrics[i]: #etsitään rivi, joka alkaa sanallamme
                for j in range(len(lyrics[i+1])):
                    if lyrics[i+1][j] == " ": #jos tulee space vastaan, niin kerätään talteen sen takana olevat sanat (tarkastellaan seuraavaa riviä)
                        testi1.append(lyrics[i+1][:j])


        #testi1 sisältää pirusti kamaa mut sen kolmas arvo sisältää vain 3 ekaa sanaa joita me halutaan käyttää
        return testi1[2]

    
    except: #errorin tullessa tyydymme vain kahden sanan aloitukseen
        try:
            return testi1[1]
        
        except: #tai yhden...
            try:
                return testi1[0]
            except: #tai jos on valittu vika rivi tekstitiedostosta
                pass


alku2 = toka_rivi_alku()


##############################################################################################################
#keskiosa
##############################################################################################################


def alkulauseen_vikasana(lause):
    for i in range(len(lause)):
        if lause[-i] == " ":
            return lause[-i+1:]


def sanachecki(index,sana):
    for j in range(len(lyrics[index])):
        for k in range(len(sana)):
            if sana[k] == lyrics[index][j+k]:
                pass
            else:
                break
        else:
            if lyrics[index][j:].count(" ") > 4:
                return True
            else:
                return False
                

def keskilause(sana):
    i_lista = []
    testi1 = []
    testi2 = []

    for i in range(len(lyrics)):
        if sana in lyrics[i]:
            for j in range(len(lyrics[i])):
                for k in range(len(sana)):
                    if sana[k] == lyrics[i][j+k]:
                        pass
                    else:
                        break
                else:
                    i_lista.append(i)


    i = random.choice(i_lista) #valitaan randomilla rivi
    aika = time.time()
    while sanachecki(i,sana) == False: #jos rivillä on alle 4 sanaa, sanamme jälkeen, arvotaan uudestaan
        if time.time()-aika >= 0.5: #jos jäädään infinite looppiin, breakataan se
            break
        
        i = random.choice(i_lista)

    for j in range(len(lyrics[i])):
        for k in range(len(sana)):
            if sana[k] == lyrics[i][j+k]:
                pass
            else:
                break
        else: #ollaan sanamme alussa rivillä
            for k in range(len(lyrics[i][j:])): #tutkitaan loppuriviä sanaltamme eteenpäin
                if len(testi1) == 3: #jos ollaan kerätty 3 seuraavaa sanaa, breakataan
                    break
                if lyrics[i][j+k] == " ": #löydetään seuraavan sanan alku
                    uus_k = k+1
                    c = 0
                    #print(testi1)
                    while True: #looppi joka etsii sanan lopun
                        try:
                            if lyrics[i][j+uus_k+c] == " ": #kun sanan loppu löydetään, lisätään testi1-listaan löydetty sana
                                testi1.append(lyrics[i][j+k:j+k+c+1])
                                break
                            else:
                                c += 1
                        except:
                            break

    return testi1






      
#interwebsistä joinkattu koodi
def listToString(s):  
    # initialize an empty string 
    str1 = ""  
    
    # traverse in the string   
    for ele in s:  
        str1 += ele   
    
    # return string   
    return str1   



keskilause_part1 = keskilause(alkulauseen_vikasana(alku1))
keskilause_part2 = keskilause(alkulauseen_vikasana(alku2))


##############################################################################################################
#loppuosa
##############################################################################################################


def keskilauseen_vikasana(lause):
        return lause[-1]

#hyväksytään sanat, jotka ovat rivin kolmas-, neljäs- tai viidesvikoja
def sanachecki_lopulle(i, sana):
    for j in range(len(lyrics[i])):
        for k in range(len(sana)):
            if sana[k] == lyrics[i][j+k]:
                pass
            else:
                break
        else:
            if 5> lyrics[i][j:].count(" ") > 3: #sanan jälkeen 4 sanaa
                return 4
            
            elif 4> lyrics[i][j:].count(" ") > 2: #sanan jälkeen 3 sanaa
                return 3
              
            elif 3> lyrics[i][j:].count(" ") > 1: #sanan jälkeen 2 sanaa
                return 2

            else:
                return False

#print("keskilauseen vika sana:",keskilauseen_vikasana(keskilause_part1))

def etsi_rivi(sana):
    i_lista = []
    testi1 =  []
        
    for i in range(len(lyrics)):
        if sana in lyrics[i]:
            for j in range(len(lyrics[i])):
                for k in range(len(sana)):
                    if sana[k] == lyrics[i][j+k]:
                        pass
                    else:
                        break
                else:
                    if lyrics[i][j+k+1] == " ":
                        i_lista.append(i)

    i = random.choice(i_lista) #valitaan randomilla rivi
    aika = time.time()
    while sanachecki_lopulle(i,sana) == False: #jos rivillä on alle 4 sanaa, sanamme jälkeen, arvotaan uudestaan
        if time.time()-aika >= 1: #jos jäädään infinite looppiin, breakataan se
            print("RUINED")
            break
        
        i = random.choice(i_lista)

    
    pituus = sanachecki_lopulle(i,sana)

    #print("lyriikoista rivi:",lyrics[i])
    #print("loppurivin pituus:",pituus)
    for j in range(len(lyrics[i])):
        for k in range(len(sana)):
            if sana[k] == lyrics[i][j+k]:
                pass
            else:
                break
        else: #ollaan sanamme alussa rivillä
            for k in range(len(lyrics[i][j:])): #tutkitaan loppuriviä sanaltamme eteenpäin
                try:
                    if len(testi1) == pituus+1: #jos ollaan kerätty kaikki paitis vika sana niin breakataan, koska tulee error muuten
                        break
                    if lyrics[i][j+k] == " ": #löydetään seuraavan sanan alku
                        uus_k = k+1
                        c = 0
                        #print(testi1)
                        while True: #looppi joka etsii sanan lopun
                            if lyrics[i][j+uus_k+c] == " ": #kun sanan loppu löydetään, lisätään testi1-listaan löydetty sana
                                testi1.append(lyrics[i][j+k:j+k+c+1])
                                break
                            else:
                                c += 1
                except:
                    break
            break


    #kerätään täällä vika sana talteen
    for j in range(len(lyrics[i])):
        if lyrics[i][-j] == " ":
            testi1.append(lyrics[i][-j:])
            break


    return testi1, i

loppu_v1,index = etsi_rivi(keskilauseen_vikasana(keskilause_part1))
def vika_lause_part2(i=index):
    testi1 = []

    try:

        for j in range(len(lyrics[i+1])):
            if lyrics[i+1][-j] == " ":
                testi1.append(lyrics[i+1][-j:])

        return testi1[2]

    except:
        try:
            return testi1[1]
        except:
            return testi1[0]


loppu1_v1 = loppu_v1[1:]
loppu1 = listToString(loppu1_v1)

loppu2 = vika_lause_part2()

keskilause_part1 = listToString(keskilause_part1)
keskilause_part2 = listToString(keskilause_part2)

print(alku1 + keskilause_part1 + loppu1)
print(alku2 + keskilause_part2 + loppu2)





