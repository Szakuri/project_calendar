'''
W tym pliku znajdziesz obsługę menu.
Aby utworzyć własny wpis w menu musisz:
1. Stworzyć nową klasę dziedziczącą po MenuCommand.
   * funkcja description() powinna zwracać napis, który zostanie wyświetlony użytkownikowi
   * funkcja execute() powinna zawierać kod, który zostanie wykonany w przypadku wywołania danej opcji w menu
2. Za pomocą funkcji add_command() dodać utworzony obiekt stworzonej przez siebie klasy do menu.
3. Polecenia menu wskazane jest przechowywać na liście np. _commands
'''




class MenuCommand:
    def description(self):
        '''Zwróć nazwę z pozycji menu'''
        raise NotImplementedError

    def execute(self):
        '''Wykonanie kodu dla danej pozycji menu'''
        raise NotImplementedError

class NewEvent(MenuCommand):
    def __init__(self, menu):
        self._menu = menu
    def description():
        return "1. New event"
    def execute(self, title, date, hours):
        self.title = title
        self.date = date
        self.hours = hours
        self.title = input("Title: ")
        self.date = input("Date (DD.MM.YYYY): ")
        self.hours = input("Time (HH.MM): ")



class ExitCommand(MenuCommand):
    def __init__(self, menu):
        '''...'''

    def description(self):
        return "Wyjście"
		

    def execute(self):
        '''...'''


class Menu:
    def __init__(self):
        self._commands = []
        self._true_run = True

    def add_command(self, cmd):
        '''...'''

    def run(self):
        while self._true_run:
   
            for i, cmd in enumerate(self._commands):
                print("{}. {}".format(i, cmd.description()))
            option = int(input("Select menu item (1-4): "))
            if option < 0 or option >= len(self._commands):
                print("Invalid input")
            else:
                self._commands[option].execute()
    def stop(self):
        '''...'''

    def _display_menu(self):
        '''...'''

    def _execute_selected_command(self):
        '''
		 Wczytanie od użytkownika numeru pozycji menu:
		cmd_num = ...
		
		Wybór i wykonanie polecenia

        cmd = ...
        cmd.execute()
        '''