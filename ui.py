""" User Interface (UI) module """


def print_table(table, title_list):
    """
    Prints table with data.

    Example:
        /-----------------------------------\
        |   id   |      title     |  type   |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/

    Args:
        table (list): list of lists - table to display
        title_list (list): list containing table headers

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    title_len_list = []
    for i in range(len(title_list)):
        title_len_list.append(len(title_list[i]))

    table_len_list = []
    list = []
    for j in range(len(table[0])):
        list += (len(table[i][j]) for i in range(len(table))) 
        table_len_list.append(max(list))

    columns_width = []
    for i in range(len(title_len_list)):
        columns_width.append(max(table_len_list[i], title_len_list[i]))

    total_width = 1
    for x in columns_width:
        total_width += x + 1

    print("/", "-" * (total_width), "\\")

    header = ""
    for i in range(len(columns_width)):
        header += "|" + title_list[i].center(columns_width[i], " ") 
    header += "|"
    print(header)

    for i in range(len(table)):
        separating_line = "|"
        row = "|"
        for j in range(len(table[i])):
            separating_line += "-" * (int(columns_width[j])) + "|"
        print(separating_line)
        for j in range(len(table[i])):
            row += table[i][j].center(int(columns_width[j]), " ") + "|"
        print(row)

    print("\\", "-" * (total_width), "/")




def print_result(result, label):
    """
    Displays results of the special functions.

    Args:
        result: result of the special function (string, list or dict)
        label (str): label of the result

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    print(label)
    print(result)


def print_menu(title, list_options, exit_message):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    print(title)
    for k, l in enumerate(list_options):
        print("({}) {}".format(k + 1, l))
    print("(0)", exit_message)


def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>

    Args:
        list_labels (list): labels of inputs
        title (string): title of the "input section"

    Returns:
        list: List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """
    inputs = []

    print(title)
    for i in range(len(list_labels)): # domyślnie liczy od zera
        inputs.append(input('Enter ' + list_labels[i] + ': ')) 

    return inputs


def print_error_message(message):
    """
    Displays an error message (example: ``Error: @message``)

    Args:
        message (str): error message to be displayed

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    print("Error: {}".format(message))
