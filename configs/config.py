
class Config():
    SQLALCHEMY_TRACK_NOTIFICATION = False

class Development(Config):
     SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123456@127.0.0.1:5432/forex'
     SECRET_KEY = 'muthomi'
     DEBUG = False
     

class Production(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123456@127.0.0.1:5432/forex'
    SECRET_KEY = 'muthomi'
    DEBUG = True