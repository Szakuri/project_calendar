

class ListingStrategy:
    def begin(self):
        pass

    def event(self, title, date, time):
        self.title = title
        self.date = date
        self.time = time
        pass

    def end(self):
        pass
    


def list_calendar(calendar, listing_strategy):
    listing_strategy.begin()

