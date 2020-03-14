from app import db, myapp
from configs.config import Development

from models.Forex import Forexx


myapp.config.from_object(Development)


def consume(a,b,c,d,e,f):
    test = Forexx(From = a,
    To = b,
    Open = c,
    High = d,
    Low = e,
    Close = f)


    db.session.add(test)
    db.session.commit()
    print('DATABASE SEEDED')


consume("KES","JPY","523365", "2652242", "562655", "5445447")
