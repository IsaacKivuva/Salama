from sqlalchemy import create_engine, Column, Integer, String, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData

Base = declarative_base()
metadata = MetaData()



class Local_doctors(Base):
    __tablename__ = "locals" 

    l_id = Column(Integer, primary_key=True)
    firstname = Column("firstname", String)
    lastname = Column(String)
    gender = Column(CHAR)
    specialities = Column(String)
    contacts = Column(Integer)

    def __init__(self, first, last, sex, speciality, contact):
        self.firstname = first
        self.lastname = last
        self.gender = sex
        self.specialities = speciality
        self.contacts = contact
        

    def __repr__(self):
        return f" {self.l_id}) {self.firstname} {self.lastname} ({self.gender}) '{self.specialities}' {self.contacts}"  

    

    

engine = create_engine('sqlite:/// locals.db', echo=True)
Base.metadata.create_all(bind=engine)

# if not engine.dialect.has_table(engine, locals):
#     metadata.create_all(engine)


Session = sessionmaker(bind = engine)
session = Session()

d1 = Local_doctors("Isaac","Kivuva", "m", "consultant", +254743502102)
d2 = Local_doctors("Sarah","Njeri", "f", "nutritionist", +254732907823)
d3 = Local_doctors("Kevin", "Odhiambo", "m", "consultant", +254720222266)
d4 = Local_doctors("Lizz", "Orlando", "f", "paeditrician", +254722903434)

session.add(d1)
session.add(d2)
session.add(d3)
session.add(d4)

session.commit()



# results = session.query(Local_doctors).all()

# def retrive_data():
#     for i in results:
#         print(i)

# print(retrive_data())
session.close()