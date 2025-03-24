import os

from flask import Flask, render_template, request

from data_models import db, Author, Book

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, 'data', 'library.sqlite')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
os.makedirs(os.path.dirname(db_path), exist_ok=True)
db.init_app(app)

# with app.app_context():
#   db.create_all()

@app.route('/add_author', methods=['GET', 'POST'])
def add_author():
    if request.method == 'GET':
        return render_template('add_author.html')

    if request.method == 'POST':
        name = request.form.get('name')
        birth_date = request.form.get('birthdate')
        date_of_death = request.form.get('date_of_death')

        author = Author(name=name, birth_date=birth_date, date_of_death=date_of_death)

        db.session.add(author)
        db.session.commit()

        return f'Author {author.name} was successfully added.'


@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'GET':
        authors = Author.query.all()
        return render_template('add_book.html', authors=authors)

    if request.method == 'POST':
        isbn = request.form.get('isbn')
        title = request.form.get('title')
        publication_year = request.form.get('publication_year')
        author_id = request.form.get('author_id')

        book = Book(isbn=isbn, title=title, publication_year=publication_year, author_id=author_id)

        db.session.add(book)
        db.session.commit()

        return f'Book {book.title} was successfully added.'

@app.route('/')
def home():
    sort_by = request.args.get('sort_by', 'title')
    search = request.args.get('search', '')

    query = Book.query

    if search:
        query = query.filter(Book.title.ilike(f'%{search}%'))

    if sort_by == 'author':
        query = query.join(Book.author).order_by(Author.name)
    else:
        query = query.order_by(Book.title)

    books = query.all()

    return render_template('home.html', books=books)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
