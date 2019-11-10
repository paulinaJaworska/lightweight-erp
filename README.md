# Lightweight ERP

Small prototype of ERP software for computer games shop. It can be handle through Command Line Interface. It's storing mechanism uses tables (list of lists) to store data in CSV format. Additionaly it is wrote without usage of built-in functions like sum(), sort(), sorted(), print(), input(), find(), index(), count().

The entry point of the software is main.py. It shows the main menu, from which we can jump to submenus (menus implemented in modules). Users can go back to the main menu from any submenu ((0) Go back to the main menu). Each submenu has a set of options. By choosing one of them you can run one of specified features like:

- Show table
- Add new item
- Update item
- Remove item.

Apart from that each submenu has some options unique for each module. They allow to preform some data analysis.
