""" Common module
implement commonly used functions here
"""
import ui

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
    generated = generated.join([rls, rlb, rn, rn, 'J', rls, '#', '&'])  
    
    #stworzenie listy zawierającej wszystkie istniejące numery id z istniejącego pliku
    for i in table:
        for k in i:
            id_collection.append(k)

    #warunek unikalności poprzez porównanie z listą 
    #jeśli wygenerowany id już istnieje, stwórz nowy
    while generated in id_collection:
        generated = generated.join([rls, rlb, rn, rn, 'J', rls, '#', '&'])  #generowanie losowego id
    
    #zwróć wygenerowany, unikalny id w formie stringa
    return generated
    
def delete_item(id_, table):    
    IDINDEX = 0
    for i in table:             #wchodzi do listy list 
        if id_[IDINDEX] in i:   #jeżeli wpisane id znajduje się w liście
            table.remove(i)     #usuń tą listę

    return table                #zwróć zaktualizowaną listę list









    

