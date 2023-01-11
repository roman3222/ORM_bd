from sqlalchemy.orm import sessionmaker
import json
from models import Publisher, Shop, Book, Stock, Sale


def load_data_from_json(session, file_path):
    with open(file_path, 'r') as dt:
        file = json.load(dt)

    for record in file:
        model = {
            'publisher': Publisher,
            'shop': Shop,
            'book': Book,
            'stock': Stock,
            'sale': Sale,
        }[record.get('model')]
        session.add(model(id=record.get('pk'), **record.get('fields')))