# Book Alchemy

Book Alchemy is a Flask-based web application that allows users to manage a personal library of books and authors. Users can add new authors and books, search and sort the list of books, and delete books (which automatically deletes the author if no books remain).

## Features

- Add new authors and books
- Search for books by title
- Sort books by title or author name
- View book covers using ISBN (via Open Library)
- Delete books and remove orphaned authors

## Tech Stack

- Python
- Flask
- SQLAlchemy
- SQLite
- HTML

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/dimitar27/Book-Alchemy.git
   cd Book-Alchemy
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   python3 app.py
   ```

4. Open your browser and navigate to:
   ```
   http://127.0.0.1:5001
   ```

---

🔗 GitHub Repository: [Book-Alchemy](https://github.com/dimitar27/Book-Alchemy.git)
