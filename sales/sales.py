""" Sales module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game sold
    * price (number): The actual sale price in USD
    * month (number): Month of the sale
    * day (number): Day of the sale
    * year (number): Year of the sale
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common

list = ["title", "price", "month", "day", "year"]
FILE_NAME_4 = "sales/sales.csv"
table = data_manager.get_table_from_file(FILE_NAME_4)

def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    list_options = ["show table", "add", "remove", "update", "get lowest price item id", "get items sold between"]
    exit_message = "Back to main menu"
    message = "There is no such option"
    title = "sales"
    ui.print_menu(title, list_options, exit_message)
    choice_input = ui.get_inputs(["Choose a special feature:"], "")
    choice = choice_input[0]
    

    if choice == '1':
        show_table(table)
    elif choice == '2':
        data_manager.write_table_to_file(FILE_NAME_4, add(table))
    elif choice == '3':
        id_ = ui.get_inputs(["Please enter an id: "], "")
        data_manager.write_table_to_file(FILE_NAME_4, common.delete_item(id_, table))
    elif choice == '4':
        update(table, id_)
    elif choice == '5':
        get_lowest_price_item_id(table)
    elif choice == '6':
        get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to)
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

    ui.print_table(table, ["id", "title", "price", "month", "day", "year"])


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    id_ = common.generate_random(table)
    title = ui.get_inputs(["Please give game's title:"],"")[0]
    price = ui.get_inputs(["Please give game's price in USD:"], "")[0]
    month = ui.get_inputs(["Please give month:"], "")[0]
    day = ui.get_inputs(["Please give day:"], "")[0]
    year = ui.get_inputs(["Please give year:"], "")[0]
    table.append([id_, title, price, month, day, year])

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

def get_lowest_price_item_id(table):
    """
    Question: What is the id of the item that was sold for the lowest price?
    if there are more than one item at the lowest price, return the last item by alphabetical order of the title

    Args:
        table (list): data table to work on

    Returns:
         string: id
    """

    # your code


def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    """
    Question: Which items are sold between two given dates? (from_date < sale_date < to_date)

    Args:
        table (list): data table to work on
        month_from (int)
        day_from (int)
        year_from (int)
        month_to (int)
        day_to (int)
        year_to (int)

    Returns:
        list: list of lists (the filtered table)
    """

    # your code
