"""
table = [['1','2'],['3','4']]

def delete(table):
    ID_INDEX = 0
    #id_to_be_erased = input("Enter id of item you wish to be erased: ")

    for i in table:
        if id_ == i[ID_INDEX]:
            table.remove(i)
            return table
    



delete(table)
print(table)
"""
table = [["kH38Jm#&"],["kH14Ju#&"]]
import random
ID_INDEX = 0

def generate_random(table):
    generated = ''

    #zmienne, z których losowane będą wartości
    id_collection = []
    letters_s = 'qwertyuiopasdfghjklzxcvbnm'
    letters_b = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    rn = str(random.randrange(0,10))
    #funkcje losujące losowe małe i duże litery
    rls = random.choice(letters_s)
    rlb = random.choice(letters_b)
    
    #generowanie losowego id
    generated = generated.join([rls, "H", rn, rn, 'J', rls, '#', '&'])  
    
    #stworzenie listy zawierającej wszystkie istniejące numery id z istniejącego pliku
    for i in table:
        for k in i:
            id_collection.append(k)

    #warunek unikalności poprzez porównanie z listą 
    #jeśli wygenerowany id już istnieje, stwórz nowy
    while generated in id_collection:
        generated = generated.join([rls, "H", rn, rn, 'J', rls, '#', '&'])  #generowanie losowego id
    
    #zwróć wygenerowany, unikalny id w formie stringa
    return generated
print(generate_random(table))









