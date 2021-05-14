from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and from create_database import Country

engine = create_engine('sqlite:///countries.db')
Session = sessionmaker(bind=engine)
session = Session()

from create_database import Country

consulta5 = session.query(Country).\
        filter(or_(Country.name.like('%uador%'),Country.capital.like('%ito%'))).all()
print(consulta5)
