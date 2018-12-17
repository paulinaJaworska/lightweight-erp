""" Human resources module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * birth_year (number)
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    title = "HR"
    list_options = ["show table", "add", "remove", "update", "get_the oldest person", "get the person closest to the average"]
    exit_message = "Back to main menu"
    ui.print_menu(title, list_options, exit_message)
    message = "There is no such option"
   
    table = data_manager.get_table_from_file("/home/kamoor13/Pulpit/ERP/lightweight-erp-python-venividivinko/hr/persons.csv")
    
    choice_input = ui.get_inputs(["Choose a special feature:"], "")
    choice = choice_input[0]
    if choice == '1':
        show_table(table)
    elif choice == '2':
        add(data_manager.write_table_to_file("/home/kamoor13/Pulpit/ERP/lightweight-erp-python-venividivinko/hr/persons.csv"), table)
    elif choice == '3':
        remove(table, id)
    elif choice == '4':
        update(table, id_)
    elif choice == '5':
        get_oldest_person
    elif choice == '6':
        get_persons_closest_to_average
    elif choice == '0':
        main.main()
    else:
        ui.print_error_message(message)


def show_table(table):  
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    ui.print_table(table, ["id", "name", "birth year"])


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    # your code

    return table


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """

    # your code

    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table (list): list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    # your code

    return table


# special functions:
# ------------------

def get_oldest_person(table):
    """
    Question: Who is the oldest person?

    Args:
        table (list): data table to work on

    Returns:
        list: A list of strings (name or names if there are two more with the same value)
    """

    # your code


def get_persons_closest_to_average(table):
    """
    Question: Who is the closest to the average age?

    Args:
        table (list): data table to work on

    Returns:
        list: list of strings (name or names if there are two more with the same value)
    """

    # your code
