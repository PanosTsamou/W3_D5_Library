class Book:

    def __init__(self, input_title, input_author, input_genre):
        self.title = input_title
        self.author = input_author
        self. genre = input_genre
        self.book_checked = False
        self.review_list = {}
        self.synopsis = ""
        
    def availability(self):
        if self.book_checked:
            return "Not Available"

        else:
            return "Available"

    def add_a_review(self, rev_text, rev_date, rev_name):
        self.review_list[rev_name]= {'text': rev_text,'date': rev_date}
    
