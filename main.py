import sqlalchemy
import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, sessionmaker

import json

from add_values import load_data_from_json
from connect import connect_db
from models import Publisher, Shop, Book, Stock, Sale
from query import get_author_books




if __name__ == '__main__':
    session = connect_db(db_name='orm_base', password='1h2j3v4f')
    # add_data = load_data_from_json(session, 'data.json')
    author_books = get_author_books(session)


    for title, shop_name, price, date_sale in author_books.all():
        print(f'{title} | {shop_name} | {price} | {date_sale}')

    session.commit()
    session.close()

