import random,time
from collections import Counter

with open("eminem_lyrics.txt", encoding="utf8") as f:
    lyrics = f.readlines()

lyrics = " ".join(lyrics).replace("\n","")

def findNextWords(lastWordCombo):
    wordCombos = []
    words = "when i "
    last_i = 7
    next2 = False 
    next1 = False
    for i in range(last_i,len(lyrics)):
        if lyrics[i] == " ":
            for k in range(len(words)):
                if words[k] == " ":
                    words = words[k+1:]
                    break
            words += lyrics[last_i:i].lower() + " "

            if next2:
                #print("third:",words)
                wordCombos.append(words)
                next2 = False

            if next1:
                #print("second:",words)
                next1 = False
                next2 = True

            if words[:-1] == lastWordCombo:
                #print("first:",words)
                next1 = True

            last_i = i+1

    return wordCombos


if __name__ == "__main__":
    #############################################################
    starter = "I hear"
    wordAmount = 100
    ############################################################

    currentCombo = starter.lower()
    finalLine = currentCombo + " "
    for _ in range(wordAmount):
        if currentCombo[-1] == " ":
            currentCombo = currentCombo[:-1]
        nextCombos = findNextWords(currentCombo)
        currentCombo = random.choice(nextCombos)
        finalLine += currentCombo

    print(finalLine)
