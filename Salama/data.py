from sqlalchemy import create_engine, ForeignKey, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
 
    
class Hospitals(Base):
    __tablename__ = "Hospitals"

    h_id = Column(Integer, primary_key=True)
    name = Column(String)
    specialists_no = Column(Integer)
    location = Column(String)
    contacts = Column(Integer)

    def __init__ (self, name, specialists, location, contact):
        self.name = name
        self.specialists_no = specialists
        self.location = location
        self.contacts = contact

    def __repr__(self):
        return f" {self.h_id}) | {self.name} : {self.specialists_no} | {self.location} | ({self.contacts}) ||"
    


class Doctors(Base):
    __tablename__ = "Doctors"

    d_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    speciality = Column(String)
    contacts = Column(Integer)
    workplace = Column(Integer, ForeignKey(Hospitals.h_id))
    
    def __init__(self, first, last, speciality, contact, workplace):
        self.first_name = first
        self.last_name = last
        self.speciality = speciality
        self.contacts = contact
        self.workplace = workplace

    def __repr__(self):
        return f" {self.d_id}) {self.first_name} {self.last_name} | {self.speciality} | {self.contacts}"
    

class Appointments(Base):
    __tablename__ = "Appointments"

    A_id = Column(Integer, primary_key=True)
    patient_name = Column(String)
    ailment = Column(String)
    doctor = Column(Integer, ForeignKey(Doctors.d_id))
    hospital = Column(Integer, ForeignKey(Hospitals.h_id))

    def __init__(self, patient, ailment, doctor, hospital):
        self.patient_name = patient
        self.ailment = ailment
        self.doctor = doctor
        self.hospital = hospital

    def  __repr__ (self):
        return f" {self.A_id}) {self.patient_name} : {self.ailment} | {self.doctor} | {self.hospital}"
    

    


engine = create_engine('sqlite:///hospitals.db' ,echo=True)
Base.metadata.create_all(bind = engine)

Session = sessionmaker(bind=engine)
session = Session()

    

