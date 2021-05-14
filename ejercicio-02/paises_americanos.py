from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and

from create_database import Country

engine = create_engine('sqlite:///countries.db')
Session = sessionmaker(bind=engine)
session = Session()

paises_americanos = session.query(Country).filter(or_(Country.continent=="NA",
    Country.continent=="SA")).all()
print(paises_americanos)

