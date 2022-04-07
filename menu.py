



from calendar import *
from menu import *



class MenuCommand:
    def __init__(self, menu):
        self.menu = menu
        


    def description(self):
        raise NotImplementedError

    def execute(self):
        raise NotImplementedError

class NewEvent(MenuCommand):
    def __init__(self, menu):
        self.menu = menu
        self.calendar = []

    def description(self):
        return "New event"

    def execute(self):
        self.title = input("Title: ")
        self.date = input("Date (DD.MM.YYYY): ")
        self.time = input("Time (HH.MM): ")
        self.event = {
            "title": self.title,
            "date": self.date,
            "time": self.time
        }
        event = self.event
        self.str_event = str("Title: "+event['title']+"\nDate: "+event['date']+", "+event['time'])
        calendar = self.calendar
        calendar.append(self.str_event)
        
        print(self.calendar)
        

class ListCalendar(MenuCommand):
    def __init__(self, menu):
        self.menu = menu

    
    def description(self):
        return "List Calendar"

    def execute(self):
        event = NewEvent(self)
        calendar = event.calendar
        print(calendar)
        
class ExportToCal:
    def __init__(self, menu):
        self.menu = menu
    
    def description(self):
        return "Export calendar to iCalendar"

    def execute(self):
        print("""
        BEGIN: VCALENDAR
        VERSION:2.0
        BEGIN:VTIMEZONE
        RZID:Europe/Warsaw
        X-LIC-LOCATION:Europe/Warsaw
        END:VTIMEZONE
        END:VCALENDAR
        """)

class ExitCommand(MenuCommand):
    def __init__(self, menu):
        self.menu = menu

    def description(self):
        return "Exit"
		

    def execute(self):
        self.menu.stop()




class Menu:
    def __init__(self):
        self._commands = []
        self._true_run = True
        self._reset_but = True

    

    def add_command(self, cmd):
        self.cmd = cmd
        self._commands.append(cmd)


    def run(self):
        while self._true_run:

            
   
            for i, cmd in enumerate(self._commands):
                print("{}. {}".format(i, cmd.description()))
            option = int(input("Select menu item (0-3): "))
            if option < 0 or option >= len(self._commands):
                print("Invalid input")
            else:
                self._commands[option].execute()

    def stop(self):
        self._true_run = False

   
    