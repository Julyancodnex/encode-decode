import time
##############################

print("entre un mot à décoder")
etat = "codé"

lettres = str(input("message encrypter: "))
final = ""
print(lettres, '?')
longd = len(lettres)
for i in range(6):
    print(i)
    time.sleep(1)
for mot in lettres:
    if mot == '£':
        mot = ' '
    if mot == '/':
        mot = 'a'
    elif mot == '*':
        mot = 'b'
    elif mot == '-':
        mot = 'c'
    elif mot == '+':
        mot = 'd'
    elif mot == '.':
        mot = 'e'
    elif mot == '¤':
        mot = 'f'
    elif mot == "¨":
        mot = 'g'
    elif mot == '&':
        mot ='h'
    elif mot == '#':
        mot = 'i'
    elif mot == '}':
        mot = 'j'
    elif mot == '{':
        mot = 'k'
    elif mot == ')':
        mot = 'l'
    elif mot == '(':
        mot = 'm'
    elif mot == ']':
        mot = 'n'
    elif mot == '[':
        mot = 'o'
    elif mot == '3':
        mot = 'p'
    elif mot == '|':
        mot = 'q'
    elif mot == '`':
        mot = 'r'
    elif mot == '_':
        mot = 's'
    elif mot == 'ç':
        mot = "t"
    elif mot == '^':
        mot = 'u'
    elif mot == '8':
        mot = 'v'
    elif mot == '@':
        mot = 'w'
    elif mot == '=':
        mot = 'x'
    elif mot == '§':
        mot = 'y'
    elif mot == '$':
        mot = 'z'
    elif mot == '5':
        mot = 'é'
    elif mot == '9':
        mot = 'à'
    final += mot
    longf = len(final)
if longd == longf:
    etat = 'décodé'
print('etat du message: ', etat)
print('\nmessage', etat, ':', final)
time.sleep(10)
