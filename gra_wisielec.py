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


print(user_word)

while hp > 0 :

    letter = input("Podaj litere: ")

    if len(find_indexes(user_letters,letter)) > 0:
        print("JUŻ SPRAWDZŁEŚ TĄ LITERE")
    else:
        user_letters.append(letter)
        print("Urzyte litery ", user_letters)
        tab = find_indexes(word,letter)

        if len(tab)==0:
            print("Nie ma takiej litery")
            hp-=1;

        for x in tab:
            user_word[x]=letter
            if "".join(user_word)==word:
                print("WIN GAME")
                sys.exit(0)
        print(user_word)

print("przegrałeś :/")
sys.exit(0)