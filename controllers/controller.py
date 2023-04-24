from flask import render_template, request, redirect, url_for
from app import app
from models.library import library_stock
from models.lib_books import *
from models.book import *
import datetime

@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')
@app.route("/events")
def events():
    return render_template('events.html')
@app.route("/aboutus")
def about_us():
    return render_template('about_us.html')

@app.route('/books')
def books():
    return render_template('library.html', title = 'Books', library = library_stock)

@app.route('/books/<index>', methods=['POST', 'GET'])
def book(index):
    if 'change' in request.form:
        if library_stock.list_of_books[int(index)].book_checked :
            library_stock.list_of_books[int(index)].book_checked = False
        else:
            library_stock.list_of_books[int(index)].book_checked =True
        return redirect(url_for('book', index=index))
    elif 'review' in request.form:
        text = request.form['review-text']
        date = datetime.date.today().strftime('%d/%m/%Y')
        name = request.form['review-name']
        library_stock.list_of_books[int(index)].add_a_review(text, datetime.date.today().strftime('%d/%m/%Y'), request.form['review-name'])
        return redirect(url_for('book', index=index))
    elif 'remove' in request.form:
        library_stock.list_of_books.remove(library_stock.list_of_books[int(index)])
        return redirect(url_for('books'))
    else:
        return render_template('book.html', book=library_stock.list_of_books[int(index)], index=index)

@app.route('/books', methods=["POST"])
def add_remove():
    if 'submit' in request.form:
        title= request.form['book-name']
        author= request.form['author-name']
        genre= request.form['genre']
        new_book = Book(title, author, genre)
        library_stock.add_a_book(new_book)
        library_stock.all_genres()
    else:
        rv_title = request.form['book-title']
        library_stock.remove_by_title(rv_title)
    return render_template('library.html', title = 'Books', library = library_stock) 

@app.route('/books/sort/<genre>', methods=['POST','GET']) 
def sorted_by_genre(genre):
    if 'submit' in request.form:
        title= request.form['book-name']
        author= request.form['author-name']
        gender= request.form['genre']
        new_book = Book(title, author, gender)
        library_stock.add_a_book(new_book)
        library_stock.all_genres()
    elif 'remove' in request.form:
        rv_title = request.form['book-title']
        library_stock.remove_by_title(rv_title)
        library_stock.all_genres()
    
    return render_template('sort_books.html', title = str(genre), library = library_stock, genre=genre)
# @app.route('/books/<index>', methods=['POST'])
# def book_actions(index):
#     print("here is the index" )
#     if 'change' in request.form:
#         book.book_checked = True if 'check-in' in request.form else  False
#         return redirect('/books/<index>')
#     return redirect('/books')
#     elif 'review' in request.form:
#         library_stock[]