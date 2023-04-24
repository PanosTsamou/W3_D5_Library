from models.book import Book
from models.lib_books import LibBooks


book1 = Book("Verity", "Colleen Hoover", "Romance")
book2 = Book("A Court of Mist and Fury", "Sarah J. Maas", "Romance")
book3 = Book("Otherlands: A World in the Making", "Thomas Halliday", "Science & Nature")
book4 = Book("Space: The Human Story", "Tim Peake", "Science & Nature")
book5 = Book("Patrick Moore's Astronomy: A Complete Introduction", "Patrick Moore", "Science & Nature")
book6 = Book("Statrs", "Ian Ridpath", "Science & Nature")
book7 = Book("Apollo Remastered", "Andy Saunders", "Science & Nature")
book8 = Book("Hello World", "Hannah Fry", "Science & Nature")
book9 = Book("Artificial Intelligence", "Melanie Mitchell", "Science & Nature")
book10 = Book("Elon Musk", "Ashlee Vance", "Biography & True Story")
book11 = Book("Fall", "John Preston", "Biography & True Story")
book12 = Book("Fall", "John Preston", "Biography & True Story")
book13 = Book("Bitcoin Billionaires", "Ben Mezrich", "Biography & True Story")
book14 = Book("My Life in Full", "Indra Nooyi", "Biography & True Story")
book15 = Book("The Future of Geography", "Tim Marshall", "Politics, Society & Education")
book16 = Book("It's OK To Be Angry  About Capitalism", "Bernie Sanders", "Politics, Society & Education")
book17 = Book("The Shortest History of Germany", "James Hawes", "Politics, Society & Education")

library_stock = LibBooks()

list_of_books = [book1, book2, book3, book4, book5, book6, book7, book8, book9, book10, book11, book12, book13, book14, book15, book16, book17]

library_stock.add_a_list_of_books(list_of_books)
library_stock.all_genres()