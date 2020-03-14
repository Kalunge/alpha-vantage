from app import db,myapp


myapp.config.from_object(Development)

from models.Forex import Forexx

def consume():
    test = Forexx(From = 'USD',
    To = 'KES',
    Open = 456325,
    High = 45625,
    Low = 56551,
    Close = 562561)

    testtwo = Forexx(From = 'USD',
    To = 'JPY',
    Open = 45211,
    High = 45522,
    Low = 32569,
    Close = 32655)

    db.session.add(test)
    db.session.add(testtwo)
    db.session.commit()
    print('DATABASE SEEDED')


if __name__ == "__main__":
    consume()
