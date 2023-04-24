class LibBooks:

    def __init__(self):
        self.list_of_books = []
        self.genders= set(())
        

    def add_a_book(self, new_book):
        self.list_of_books.append(new_book)

    def add_a_list_of_books(self, new_list_of_books):
        self.list_of_books.extend(new_list_of_books)

    def remove_a_book(self, remove_book):
        self.list_of_books.remove(remove_book)

    def remove_by_title(self, rv_title):
        for book in self.list_of_books:
            if book.title == rv_title:
                self.list_of_books.remove(book)

    def all_genders(self):
        for book in self.list_of_books:
            self.genders.add(book.gender)
    
