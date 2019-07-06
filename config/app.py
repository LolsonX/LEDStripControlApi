class Config(object):
    POSTGRES_USER = 'postgres'
    POSTGRES_PW = 'postgres'
    POSTGRES_URL = 'localhost:5432'
    POSTGRES_DB = 'LEDApi'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,
                                                                                    pw=POSTGRES_PW,
                                                                                    url=POSTGRES_URL,
                                                                                    db=POSTGRES_DB)