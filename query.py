from sqlalchemy.orm import sessionmaker
from models import Publisher, Shop, Book, Stock, Sale


def get_author_books(session):
    author_name = input('Введите имя издателя: ')
    author_books = session.query(Book.title, Shop.name, Sale.price, Sale.date_sale) \
        .join(Publisher, Book.id_publisher == Publisher.id) \
        .join(Stock, Stock.id_book == Book.id) \
        .join(Shop, Stock.id_shop == Shop.id) \
        .join(Sale, Sale.id_stock == Stock.id) \
        .filter(Publisher.name == author_name)

    return author_books
