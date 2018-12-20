""" Accounting module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * month (number): Month of the transaction
    * day (number): Day of the transaction
    * year (number): Year of the transaction
    * type (string): in = income, out = outflow
    * amount (int): amount of transaction in USD
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common

FILE_NAME = "accounting/items.csv"
table = data_manager.get_table_from_file(FILE_NAME)
labels = ["month", "day", "year", "type", "amount in USD"]


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    special_features = ["show table", "add record", "remove record", "update", "which year max", "avg amount"]
    ui.print_menu("Accounting", special_features, "Back to main menu")
    message = "There is no such option"

    

    choice_input = ui.get_inputs(["Choose a special feature:"], "")
    choice = choice_input[0]
    if choice == '1':
        show_table(table)
    elif choice == '2':
        #table = add(table)
        data_manager.write_table_to_file(FILE_NAME, common.add_item(labels, table))
    elif choice == '3':
        id_ = ui.get_inputs(["Please enter an id: "], "")
        data_manager.write_table_to_file(FILE_NAME, common.delete_item(id_, table))
    elif choice == '4':
        id_ = ui.get_inputs(["Please enter an id: "], "")
        common.update(id_, table, labels)
    elif choice == '5':
        which_yearmax(table, id_)
    elif choice == '6':
        avg_amount(table, year)
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
    ui.print_table(table, ["id", "month", "day", "year", "type", "amount"])


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
    return common.delete_item(id_, table)
    


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table (list): list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """
    return table
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
"""

# special functions:
# ------------------

def which_year_max(table):
    """
    Question: Which year has the highest profit? (profit = in - out)

    Args:
        table (list): data table to work on

    Returns:
        number
    """

    # your code


def avg_amount(table, year):
    """
    Question: What is the average (per item) profit in a given year? [(profit)/(items count)]

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        number
    """

    # your code
