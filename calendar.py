'''
W tym pliku znajdziesz kod odpowiedzialny za wyświetlanie zdarzeń z kalendarza.

Do zmiany zachowania funkcji list_calendar wykorzystaj strategię ListingStrategy.

'''

class ListingStrategy:
    def begin(self):
        pass

    def event(self, title, date, time):
        pass

    def end(self):
        pass


def list_calendar(calendar, listing_strategy):
    listing_strategy.begin()

