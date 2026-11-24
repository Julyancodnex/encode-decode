# importation
#saisie
#chronometre
#l'algorithme
#afficher le message du depart
#afficher le message de fin
###################################################
import time

print("entre un mot à coder")
etat = "non codé"
lettres = str(input("message: "))
final = ""
print(lettres, '?')
long = len(lettres)
for i in range(6):
    print(i)
    time.sleep(1)

for mot in lettres:
    if mot == ' ':
        mot = '£'
    if mot == 'a':
        mot = '/'
    elif mot == 'b':
        mot = '*'
    elif mot == 'c':
        mot = '-'
    elif mot == 'd':
        mot = '+'
    elif mot == 'e':
        mot = '.'
    elif mot == 'f':
        mot = '¤'
    elif mot == 'g':
        mot = "¨"
    elif mot == '&':
        mot = '~'
    elif mot == 'i':
        mot = '#'
    elif mot == 'j':
        mot = '}'
    elif mot == 'k':
        mot = '{'
    elif mot == 'l':
        mot = ')'
    elif mot == 'm':
        mot = '('
    elif mot == 'n':
        mot = ']'
    elif mot == 'o':
        mot = '['
    elif mot == 'p':
        mot = '3'
    elif mot == 'q':
        mot = '|'
    elif mot == 'r':
        mot = '`'
    elif mot == 's':
        mot = '_'
    elif mot == 't':
        mot = "ç"
    elif mot == 'u':
        mot = '^'
    elif mot == 'v':
        mot = '8'
    elif mot == 'w':
        mot = '@'
    elif mot == 'x':
        mot = '='
    elif mot == 'y':
        mot = '§'
    elif mot == 'z':
        mot = '$'
    elif mot == 'é':
        mot = '5'
    elif mot == 'à':
        mot = '9'
    final += mot
etat = 'codé'
print('etat du message: ', etat)
print('\nmessage', etat, ':', final)
time.sleep(10)
for i in range(3):
    print("\n")