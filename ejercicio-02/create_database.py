from sqlalchemy import create_engine

engine = create_engine('sqlite:///countries.db')

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, Integer, String, Float

class Country(Base):
    __tablename__ = 'Country'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    capital = Column(String)
    continent = Column(String)
    dial = Column(String)
    geoname_id = Column(Float)
    itu = Column(String)
    languages = Column(String)
    independent = Column(String)
    def __repr__(self):
        return "Country: name=%s Capital=%s Continent:%s dial=%s geoname_id=%f itu=%s languages=%s independent=%s \n" % (
                          self.name,
                          self.capital,
                          self.continent,
                          self.dial,
                          self.geoname_id,
                          self.itu,
                          self.languages,
                          self.independent)

Base.metadata.create_all(engine)
