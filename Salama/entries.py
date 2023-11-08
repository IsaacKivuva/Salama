from data import *



hospitals_data = [
    ("Aga Khan", 1, "Nairobi", "+254020030020"),
    ("MP-SHAH", 2, "Westlands", "+254730020020"),
    ("Getrudes", 3, "Embakasi", "+254799966633"),
    ("Nairobi-Hospital", 2, "Nairobi", "+25400000001"),
    ("KNH", 2, "Upper-Hill", "+25430030030")
]


for name, category, location, contact in hospitals_data:
    h = Hospitals(name, category, location, contact)

    existing_data = session.query(Hospitals).filter_by(name=name).first()

    if existing_data is None:
        session.add(h)
        session.commit()



doctors_data = [
    ("Mary", "Wanjiru", "physiotherapist", "+254722226693", 1),
    ("Fred", "Otieno", "Gynaecology", "+25410628132", 2),
    ("Michael", "Njoroge", "Radiology", "+254730805105", 5),
    ("Benjamin", "Amani", "Dentistry", "+254720201301", 3),
    ("Sarah", "Murimi", "Dermatology", "+254738008080", 3),
    ("Maureen", "Natalie", "Neurology", "+25478340049", 3),
    ("Brian", "Kipyegon", "Neurology", "+25478394034", 4),
    ("Vera", "Akinyi", "Gynaecology", "+254789040821", 2),
    ("Kimberly", "Wanjiru", "physiotherapist", "+25493803748", 5),
    ("Samson", "Strong", "Dentistry", "+25420802093", 4)
]


for first_name, last_name, specialization, phone, hospital_id in doctors_data:
    d = Doctors(first_name, last_name, specialization, phone, hospital_id)
    
    existing_data = session.query(Doctors).filter_by(first_name=first_name, last_name=last_name).first()

    if existing_data is None:
        session.add(d)
        session.commit()


session.close()