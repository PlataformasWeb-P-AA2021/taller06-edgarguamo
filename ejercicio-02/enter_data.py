from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from create_database import Country

import json
import requests
# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine('sqlite:///countries.db')

Session = sessionmaker(bind=engine)
session = Session()

df = requests.get('https://pkgstore.datahub.io/core/country-codes/country-codes_json/data/616b1fb83cbfd4eb6d9e7d52924bb00a/country-codes_json.json')
data = df.json()

for d in data:
    print(d['Capital'])
    p = Country(name=d['CLDR display name'],capital=d['Capital'],continent=d['Continent'],
            dial = d['Dial'], geoname_id=d['Geoname ID'], itu = d['ITU'],
            languages = d['Languages'], independent = d['is_independent'])
    session.add(p)

session.commit()


