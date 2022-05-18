import sys
hp = 5
word = "dupa"
user_word = []
user_letters = []
test_string = "";
for _ in word:
    user_word.append("_")

def find_indexes(word, letter):
    indexes = []
    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)
    return indexes

def stastus_geme():
    print()
    print("Hp:",hp)
    print("Urzyte literu:",user_letters)
    print(user_word)
    print()


print(user_word)

while hp > 0 :

    letter = input("Podaj litere: ")

    if len(find_indexes(user_letters,letter)) > 0:
        print("JUŻ SPRAWDZŁEŚ TĄ LITERE")
    else:
        user_letters.append(letter)
        tab = find_indexes(word,letter)

        if len(tab)==0:
            print("Nie ma takiej litery")
            hp-=1;

        for x in tab:
            user_word[x]=letter
            if "".join(user_word)==word:
                print("WIN GAME")
                sys.exit(0)
    stastus_geme()

print("przegrałeś :/")
sys.exit(0)