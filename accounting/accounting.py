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

FILE_NAME = "/home/kamoor13/Pulpit/ERP/lightweight-erp-python-venividivinko/accounting/items.csv"
table = data_manager.get_table_from_file(FILE_NAME)



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
        data_manager.write_table_to_file(FILE_NAME, add(table))
    elif choice == '3':
        remove(table, id)
    elif choice == '4':
        updatetable(table, id_)
    elif choice == '5':
        which_yearmax(table, id)
    elif choice == '6':
        avg_amount(table, year)
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
    ui.print_table(table, ["id", "month", "day", "year", "type", "amount"])


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """
    #file_name = "old_lightweight-erp-python-venividivinko/accounting/items.csv"
    #table = data_manager.get_table_from_file(file_name)
    id_ = common.generate_random(table)
    month = ui.get_inputs(["month:"],"")[0]
    day = ui.get_inputs(["Please give day:"], "")[0]
    year = ui.get_inputs(["Please give year:"], "")[0]
    type1 = ui.get_inputs(["Please give type: inflow (in)/outflow (out):"], "")[0]
    amount = ui.get_inputs(["Please give the amountof transaction in USD:"], "")[0]
    table.append([id_, month, day, year, type1, amount])
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
    IDINDEX = 0

    id_ = ui.get_inputs(["Please enter an id: "], "")

    for i in table:
        if id_ == i[IDINDEX]:
            table.remove(i)

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
