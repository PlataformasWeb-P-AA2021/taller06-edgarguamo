from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and

from create_database import Country

engine = create_engine('sqlite:///countries.db')
Session = sessionmaker(bind=engine)
session = Session()

paises_asiaticos = session.query(Country).filter(Country.continent == 'AS').\
        order_by(Country.dial).all()

for p in paises_asiaticos:
    print("%s, %s" % (p.name, p.dial))
