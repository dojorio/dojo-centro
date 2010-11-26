book, book1, book2 = range(3)

class Chart():
    def __init__(self):
        self.books = []

    def add(self, book):
        self.books.append(book)
        
    def __len__(self):
        return len(self.books)
    

class BookCharger(object):
    def __init__(self, chart):
        # rates = {1 : 1, 2: .95, 3: .90, 4: .80, 5: .75}
        rates = {1 : 1, 2: .95}
        book_price = 42
        number_of_different_books = len(set(chart.books))
        rate = rates.get(number_of_different_books, 0)
        self.price = book_price * rate * number_of_different_books
        
        if number_of_different_books < len(chart.books):
            self.price += 42
        

           
