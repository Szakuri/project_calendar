
from menu import ListCalendar, Menu, NewEvent, ExitCommand
from calendar import *





def main():


  

    menu = Menu()

    menu.add_command(NewEvent(menu))
    menu.add_command(ListCalendar(menu))
    menu.add_command(ExitCommand(menu))


    


    menu.run()




if __name__ == "__main__":
    main()






