""" Store module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game
    * manufacturer (string)
    * price (number): Price in dollars
    * in_stock (number)
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common

labels = ["title", "manufacturer", "price", "in_stock"]

def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    special_features = ["show table", "add record", "remove record", "update", "get counts by manufacturers", "get average by manufacturers"]
    ui.print_menu("Store", special_features, "Back to main menu")
    message = "There is no such option"

    table = data_manager.get_table_from_file("/home/kamoor13/Pulpit/ERP/lightweight-erp-python-venividivinko/store/games.csv")

    choice_input = ui.get_inputs(["Choose a special feature:"], "")
    choice = choice_input[0]
    if choice == '1':
        show_table(table)
    elif choice == '2':
        add(data_manager.write_table_to_file("/home/kamoor13/Pulpit/ERP/lightweight-erp-python-venividivinko/store/games.csv"), table)
    elif choice == '3':
        remove(table, id)
    elif choice == '4':
        update(table, id_)
    elif choice == '5':
        get_counts_by_manufacturers()
    elif choice == '6':
        get_average_by_manufacturer()
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

    ui.print_table(table, ["id", "title", "manufacturer", "price in $", "in stock"])


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
        table: list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    IDINDEX = 0
    list = []
    list = list + id_
    for row in table:
        if id_[IDINDEX] in row:
            list = list + ui.get_inputs(labels, "Please provide updated information: ")
            for i in range(len(row)):
                row[i] = list[i]

    return table


# special functions:
# ------------------

def get_counts_by_manufacturers(table):
    """
    Question: How many different kinds of game are available of each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
         dict: A dictionary with this structure: { [manufacturer] : [count] }
    """

    # your code


def get_average_by_manufacturer(table, manufacturer):
    """
    Question: What is the average amount of games in stock of a given manufacturer?

    Args:
        table (list): data table to work on
        manufacturer (str): Name of manufacturer

    Returns:
         number
    """

    # your code
