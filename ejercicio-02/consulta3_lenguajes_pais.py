from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, selectinload
from sqlalchemy import and_, or_ # se importa el operador and

from create_database import Country

engine = create_engine('sqlite:///countries.db')
Session = sessionmaker(bind=engine)
session = Session()

lenguajes_pais = session.query(Country).all()

for s in lenguajes_pais:
    print("%s, %s" %(s.name, s.languages))
