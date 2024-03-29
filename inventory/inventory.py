""" Inventory module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string): Name of item
    * manufacturer (string)
    * purchase_year (number): Year of purchase
    * durability (number): Years it can be used
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common

FILE_NAME_3 = "inventory/inventory.csv"
table = data_manager.get_table_from_file(FILE_NAME_3)

def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    special_features = ["show table", "add record", "remove record", "update", "get available items", "get average durability by manufacturers"]
    ui.print_menu("Inventory", special_features, "Back to main menu")
    message = "There is no such option"
    choice_input = ui.get_inputs(["Choose a special feature:"], "")
    choice = choice_input[0]
    

    if choice == '1':
        show_table(table)
    elif choice == '2':
        data_manager.write_table_to_file(FILE_NAME_3, common.add_item(labels, table))
    elif choice == '3':
        id_ = ui.get_inputs(["Please enter an id: "], "")
        data_manager.write_table_to_file(FILE_NAME_3, common.delete_item(id_, table))
    elif choice == '4':
        id_ = ui.get_inputs(["Please enter an id: "], "")
        common.update(id_, table, labels)
    elif choice == '5':
        get_available_items(table)
    elif choice == '6':
        get_average_durability_by_manufacturers(table)
    elif choice == '0':
        common.menu_back()
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

    ui.print_table(table, ["id", "name", "manufacturer", "purchase year", "durability"])


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

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

def get_available_items(table):
    """
    Question: Which items have not exceeded their durability yet?

    Args:
        table (list): data table to work on

    Returns:
        list: list of lists (the inner list contains the whole row with their actual data types)
    """

    # your code


def get_average_durability_by_manufacturers(table):
    """
    Question: What are the average durability times for each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
        dict: a dictionary with this structure: { [manufacturer] : [avg] }
    """

    # your code
