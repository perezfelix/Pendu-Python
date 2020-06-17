import random

def words_randomised():
    word_letters = ""
    count = 0
    liste = open("words.txt", "r")
    word = random.randrange(0, 834)
    for i in liste:
        if count == word:
            word_letters = i
            count += 1
        else:
            count += 1 
    liste.close()
    return word_letters

def req(word, letter):
    letter_pos = []
    count = 0
    for i in word:
        if i == letter:
            letter_pos.append(count)
            count += 1
        else:
            count += 1
    if letter_pos == []:
        return False
    else:
        return letter_pos