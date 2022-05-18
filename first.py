hp = 5
word = "dupa"
user_word=[]

for letter in word:
    user_word.append("_")

print(user_word)

while hp > 0 :
    letter = input("Podaj litere: ")

    hp-=1