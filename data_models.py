from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()

class Author(db.Model):
    """Represents an author in the library."""
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column()
    birth_date: Mapped[str] = mapped_column()
    date_of_death: Mapped[str] = mapped_column()

    def __repr__(self):
        return f'Author id: {self.id}, Author name: {self.name}, Author birth date: {self.birth_date}, Author date of death: {self.date_of_death}'

class Book(db.Model):
    """Represents a book with a foreign key reference to its author."""
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    isbn: Mapped[str] = mapped_column()
    title: Mapped[str] = mapped_column()
    publication_year: Mapped[str] = mapped_column()
    author_id: Mapped[int] = mapped_column(ForeignKey("author.id"))
    author: Mapped["Author"] = relationship()

    def __repr__(self):
        return f'Book id: {self.id}, title: {self.title}, isbn: {self.isbn}, year: {self.publication_year}, author_id: {self.author_id}'
