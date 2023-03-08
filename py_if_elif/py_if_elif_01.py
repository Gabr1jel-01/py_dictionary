# dog_barks = True


# if dog_barks:
#     print('Close the window')
# else:
#     print('Leave open')
    
# a = 5

# if a > 3:
#     print('a je vece od 3')
# else:
#     print('a NIJE vece od 3')
       
numbers = list(range(1, 31))

for number in numbers:
    if number % 3 == 0:
        print(number)
    if number % 6 == 0:
        print(number)
    if number % 9 == 0:
        print(number)
    else:
        print('Broj nije djeljiv sa 3 6 ili 9')
        
        
        
        
# Kreirajtelistu od 1 do broja 30. Ispišitesvebrojevekoji sudjeljivis 3, 6 i9
# •
# Provjera je li broj djeljivs nekim drugim radimo pomoću % (modulo) operanda.
# •
# 15 % 3 NEMA ostatka, odnosno to je 0 pa je 15 djeljiv s 3.
# •
# 16 % 3 je 1, odnosno NIJE jednak 0 pa 16 NIJE djeljiv s 3.
# •
# Napišite program koji provjerava pripada li unesena riječ vrsti riječi palindrom.
# •
# Palindromje riječ koja se jednako piše(i čita) s lijeva na desno i s desna na lijevo.



word = input('Upisite jednu rijec')

reversed_word = word[ : : -1]

if word == reversed_word:
    print(f'Rijec {word} JE palindrom')
else:
    print(f'Rijec {word} NIJE palindrom')
    
