from fonctions import words_randomised, req

score = 0
vies = 8
print("Bienvenu dans le jeu du pendu")
start = input("Voulez vous commencer ? (y/n) : ")
if start == "y":
    start = True
else: 
    start = False
while start:
    win = True
    lose = True
    word = words_randomised()
    word = word[:-1]
    print_word = {}
    c = 0
    wintest = 0
    for x in word:
        print_word["string{0}".format(c)] = "_"
        c += 1
    while win or lose:
        print(" ")
        print("votre score actuel est de {0}".format(score))
        print(" ")
        print("Vous avez {0} vies restantes".format(vies))
        print(" ")
        for k in print_word.values():
            print(k, end = ' ')
        print(" ")
        letter = input("Quelle est la lettre que vous voulez soummettre ? : ")
        letter = letter.capitalize()
        request = req(word, letter)
        if request == False:
            vies += -1
            print("Perdu, votre lettre n'est pas incluse dans le mot, il vous reste {0} vies".format(vies))
        else:
            for i in request:
                print_word["string{0}".format(i)] = letter
                if print_word["string{0}".format(i)] != "_":
                    wintest += 1
        if vies <= 0:
            print("Perdu")
            break
        elif wintest == len(word):
            print("Vous avez gagner !")
            score += 1
            break
    start = input("Voulez vous rejouer ? (y/n) : ")
    if start == "y":
        start = True
    else: 
        start = False
    