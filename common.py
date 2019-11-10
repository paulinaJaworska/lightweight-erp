""" Common module
implement commonly used functions here
"""
import ui
import main
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

def add_item(labels, table):
    id_ = generate_random(table)                                                #załaduj unikalny ID
    new_record = ui.get_inputs(labels, "Now enter following information")       #wprowadzenie danych z terminala
    new_record.insert(0,id_)                                                    #dodaj dane do listy
    table.append(new_record)                                                    #zaktualizuj listę list o nową listę
    return table                                                                #zwróć zaktualizowaną listę list

def update(id_, table, labels):
    ID_INDEX = 0
    list = []     
    list += id_
    for row in table:
        if id_[ID_INDEX] in row:
            list += ui.get_inputs(labels, "Please provide updated information: ")
            for i in range(len(row)):
                row[i] = list[i]

    return table

def menu_back():
    main.main()




#################################

import data_manager


question_labels = ["id", "submission_time", "view_number", "vote_number", "title", "message", "image"]
answer_labels = ["id", "submission_time", "vote_number", "question_id", "message", "image"]
# parameters to call the import data: filename = "data/answers.csv" or filename = "data/questions.csv"


sample_data_question = 'sample_data/question.csv'
sample_data_answer = 'sample_data/answer.csv'

### SORTING  ###
def sort_list_of_dict(list_of_dictionaries, sort_by, order):
    '''
    Sorts list of dictionaies by given parameter in ascending or descending order.
    :param list_of_dictionaries:
    :param sort_by: key by which we want to sort by
    :param order: boolean (True or False)  True = descending
    :return: sorted list of dicts
    '''
    return sorted(list_of_dictionaries, key=lambda i: i[str(sort_by)], reverse=order)



###  FUNCTIONS READING CSV FILES AND   ###
not_sorted_question_data = data_manager.import_data(sample_data_question)
question_data = sort_list_of_dict(not_sorted_question_data, "submission_time", True )

answer_data = data_manager.import_data(sample_data_answer)





### Pulling from database  ###



###   WRITING TO CSV   ###

def id_generator(filename):
    exists = os.path.isfile(filename)
    if not exists:
        return 1
    else:
        with open(filename, 'r') as f:
            result = csv.DictReader(f)
            for row in result:
                result = row["id"]
            return result + 1

def date_generator():
    time_stamp = time.time()
    return int(time_stamp)


def prepare_data_for_questions_data(question_data_from_form):
    """
    Append necessary data, which is not enter by user, to data from question form filled by user.
    :param question_data_from_form: dictionary
    :return: dictionary
    """
    next_id = id_generator()
    submission_time = date_generator()
    view_number = "not implemented"
    vote_number = "not implemented"
    image = "no image"
    generated_automatically = {'id': next_id, "submission_time": submission_time, "view_number": view_number,
                               "vote_number": vote_number, "image": image}
    question_data_from_form.update(generated_automatically)
    return question_data_from_form


def prepare_answer_to_be_saved_in_csv(question_data):
    next_id = id_generator()
    submission_time = date_generator()



    #######################################################

import csv
import os


def import_data(filename):
    exists = os.path.isfile(filename)
    if not exists:
        return None
    else:
        with open(filename, 'r') as f:
            read_dictionary = csv.DictReader(f)
            result = []
            for row in read_dictionary:
                result.append(dict(row))
            return result


def export_data(filename, labels, some_data_to_add):
    exists = os.path.isfile(filename)
    with open(filename, "a+") as f:
        writer = csv.DictWriter(f, fieldnames=labels, delimiter=',')
        if not exists:
            writer.writeheader()
        writer.writerow(some_data_to_add)



    

