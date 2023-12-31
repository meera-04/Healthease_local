
# def insert_doctors():
#   doctors_data = [
#       "full_name": "Dr. Rajesh Kumar",
#         "age": 45,
#         "username": "rajesh_kumar",
#         "password": "rajesh123",
#         "email": "rajesh.kumar@example.com",
#         "role": "doctor",
#         "experience": 18,
#         "speciality": "Cardiology",
#         "department": "Cardiology Department",
#         "department_id": "C101",
#         "hospital": "City Heart Hospital",
#         "available_slots": ["09:00 AM", "10:00 AM", "11:00 AM", "02:00 PM", "03:00 PM"],
#         "booked_slots": [],
#         "appointment_duration": 30,
#         "appointment_fee": 1000,
#     },
#     {
#         "full_name": "Dr. Sneha Patel",
#         "age": 38,
#         "username": "sneha_patel",
#         "password": "sneha123",
#         "email": "sneha.patel@example.com",
#         "role": "doctor",
#         "experience": 12,
#         "speciality": "Cardiology",
#         "department": "Cardiology Department",
#         "department_id": "C102",
#         "hospital": "Apex Cardiac Institute",
#         "available_slots": ["10:00 AM", "11:00 AM", "02:00 PM", "03:00 PM", "04:00 PM"],
#         "booked_slots": [],
#         "appointment_duration": 30,
#         "appointment_fee": 900,
#     },
#     {
#         "full_name": "Dr. Anand Sharma",
#         "age": 42,
#         "username": "anand_sharma",
#         "password": "anand123",
#         "email": "anand.sharma@example.com",
#         "role": "doctor",
#         "experience": 20,
#         "speciality": "Cardiology",
#         "department": "Cardiology Department",
#         "department_id": "C103",
#         "hospital": "Global Heart Care Center",
#         "available_slots": ["09:00 AM", "10:00 AM", "02:00 PM", "03:00 PM", "04:00 PM"],
#         "booked_slots": [],
#         "appointment_duration": 45,
#         "appointment_fee": 1200,
#     },
#     {
#         "full_name": "Dr. Snehal Shah",
#         "age": 41,
#         "username": "snehal_shah",
#         "password": "snehal123",
#         "email": "snehal.shah@example.com",
#         "role": "doctor",
#         "experience": 14,
#         "speciality": "Cardiology",
#         "department": "Cardiology Department",
#         "department_id": "C104",
#         "hospital": "CardioMed Hospital",
#         "available_slots": ["09:00 AM", "10:00 AM", "02:00 PM", "03:00 PM", "04:00 PM"],
#         "booked_slots": [],
#         "appointment_duration": 30,
#         "appointment_fee": 850,
#     },
#     {
#         "full_name": "Dr. Deepika Mehta",
#         "age": 39,
#         "username": "deepika_mehta",
#         "password": "deepika123",
#         "email": "deepika.mehta@example.com",
#         "role": "doctor",
#         "experience": 11,
#         "speciality": "Cardiology",
#         "department": "Cardiology Department",
#         "department_id": "C105",
#         "hospital": "HeartCare Clinic",
#         "available_slots": ["09:00 AM", "10:00 AM", "11:00 AM", "02:00 PM", "03:00 PM"],
#         "booked_slots": [],
#         "appointment_duration": 30,
#         "appointment_fee": 950,
#     },
#     {
#         "full_name": "Dr. Mohan Reddy",
#         "age": 50,
#         "username": "mohan_reddy",
#         "password": "mohan123",
#         "email": "mohan.reddy@example.com",
#         "role": "doctor",
#         "experience": 22,
#         "speciality": "Dermatology",
#         "department": "Dermatology Department",
#         "department_id": "D201",
#         "hospital": "Dermacare Hospital",
#         "available_slots": ["10:00 AM", "11:00 AM", "02:00 PM", "03:00 PM", "04:00 PM"],
#         "booked_slots": [],
#         "appointment_duration": 30,
#         "appointment_fee": 800,
#     },
#     {
#         "full_name": "Dr. Nidhi Verma",
#         "age": 33,
#         "username": "nidhi_verma",
#         "password": "nidhi123",
#         "email": "nidhi.verma@example.com",
#         "role": "doctor",
#         "experience": 8,
#         "speciality": "Dermatology",
#         "department": "Dermatology Department",
#         "department_id": "D202",
#         "hospital": "Glowing Skin Clinic",
#         "available_slots": ["10:00 AM", "11:00 AM", "02:00 PM", "03:00 PM", "04:00 PM"],
#         "booked_slots": [],
#         "appointment_duration": 30,
#         "appointment_fee": 750,
#     },
#     {
#         "full_name": "Dr. Sneha Sharma",
#         "age": 36,
#         "username": "sneha_sharma",
#         "password": "sneha123",
#         "email": "sneha.sharma@example.com",
#         "role": "doctor",
#         "experience": 9,
#         "speciality": "Dermatology",
#         "department": "Dermatology Department",
#         "department_id": "D203",
#         "hospital": "SkinCare Hospital",
#         "available_slots": ["10:00 AM", "11:00 AM", "02:00 PM", "03:00 PM", "04:00 PM"],
#         "booked_slots": [],
#         "appointment_duration": 30,
#         "appointment_fee": 850,
#     },
#     {
#         "full_name": "Dr. Siddharth Gupta",
#         "age": 39,
#         "username": "siddharth_gupta2",
#         "password": "siddharth123",
#         "email": "siddharth.gupta2@example.com",
#         "role": "doctor",
#         "experience": 10,
#         "speciality": "Orthopedics",
#         "department": "Orthopedics Department",
#         "department_id": "O303",
#         "hospital": "OrthoCare Hospital",
#         "available_slots": ["09:00 AM", "10:00 AM", "02:00 PM", "03:00 PM", "04:00 PM"],
#         "booked_slots": [],
#         "appointment_duration": 45,
#         "appointment_fee": 1200,
#     },
#     {
#         "full_name": "Dr. Meera Singh",
#         "age": 36,
#         "username": "meera_singh",
#         "password": "meera123",
#         "email": "meera.singh@example.com",
#         "role": "doctor",
#         "experience": 9,
#         "speciality": "Orthopedics",
#         "department": "Orthopedics Department",
#         "department_id": "O304",
#         "hospital": "Joint Health Center",
#         "available_slots": ["09:00 AM", "10:00 AM", "02:00 PM", "03:00 PM", "04:00 PM"],
#         "booked_slots": [],
#         "appointment_duration": 45,
#         "appointment_fee": 1000,
#     },
#    {
#         "full_name": "Dr. Akshay Sharma",
#         "age": 40,
#         "username": "akshay_sharma",
#         "password": "akshay123",
#         "email": "akshay.sharma@example.com",
#         "role": "doctor",
#         "experience": 15,
#         "speciality": "Cardiology",
#         "department": "Cardiology Department",
#         "department_id": "C106",
#         "hospital": "Heartbeat Hospital",
#         "available_slots": ["09:00 AM", "10:00 AM", "11:00 AM", "02:00 PM", "03:00 PM"],
#         "booked_slots": [],
#         "appointment_duration": 30,
#         "appointment_fee": 1100,
#     },
#     {
#         "full_name": "Dr. Ritu Gupta",
#         "age": 37,
#         "username": "ritu_gupta",
#         "password": "ritu123",
#         "email": "ritu.gupta@example.com",
#         "role": "doctor",
#         "experience": 11,
#         "speciality": "Cardiology",
#         "department": "Cardiology Department",
#         "department_id": "C107",
#         "hospital": "Heartline Clinic",
#         "available_slots": ["10:00 AM", "11:00 AM", "02:00 PM", "03:00 PM", "04:00 PM"],
#         "booked_slots": [],
#         "appointment_duration": 30,
#         "appointment_fee": 950,
#     },
#     {
#         "full_name": "Dr. Rahul Singh",
#         "age": 44,
#         "username": "rahul_singh",
#         "password": "rahul123",
#         "email": "rahul.singh@example.com",
#         "role": "doctor",
#         "experience": 19,
#         "speciality": "Cardiology",
#         "department": "Cardiology Department",
#         "department_id": "C108",
#         "hospital": "City Cardiac Care",
#         "available_slots": ["09:00 AM", "10:00 AM", "02:00 PM", "03:00 PM", "04:00 PM"],
#         "booked_slots": [],
#         "appointment_duration": 45,
#         "appointment_fee": 1150,
#     },
#     {
#         "full_name": "Dr. Ananya Gupta",
#         "age": 38,
#         "username": "ananya_gupta",
#         "password": "ananya123",
#         "email": "ananya.gupta@example.com",
#         "role": "doctor",
#         "experience": 13,
#         "speciality": "Dermatology",
#         "department": "Dermatology Department",
#         "department_id": "D204",
#         "hospital": "Glow Skin Clinic",
#         "available_slots": ["10:00 AM", "11:00 AM", "02:00 PM", "03:00 PM", "04:00 PM"],
#         "booked_slots": [],
#         "appointment_duration": 30,
#         "appointment_fee": 850,
#     },
#     {
#         "full_name": "Dr. Aryan Singh",
#         "age": 43,
#         "username": "aryan_singh",
#         "password": "aryan123",
#         "email": "aryan.singh@example.com",
#         "role": "doctor",
#         "experience": 17,
#         "speciality": "Dermatology",
#         "department": "Dermatology Department",
#         "department_id": "D205",
#         "hospital": "Glowing DermaCare",
#         "available_slots": ["10:00 AM", "11:00 AM", "02:00 PM", "03:00 PM", "04:00 PM"],
#         "booked_slots": [],
#         "appointment_duration": 30,
#         "appointment_fee": 900,
#     },
#     {
#         "full_name": "Dr. Rishi Sharma",
#         "age": 39,
#         "username": "rishi_sharma",
#         "password": "rishi123",
#         "email": "rishi.sharma@example.com",
#         "role": "doctor",
#         "experience": 14,
#         "speciality": "Dermatology",
#         "department": "Dermatology Department",
#         "department_id": "D206",
#         "hospital": "Skin Health Clinic",
#         "available_slots": ["10:00 AM", "11:00 AM", "02:00 PM", "03:00 PM", "04:00 PM"],
#         "booked_slots": [],
#         "appointment_duration": 30,
#         "appointment_fee": 950,
#     },
#     {
#         "full_name": "Dr. Siddharth Gupta",
#         "age": 39,
#         "username": "siddharth_gupta2",
#         "password": "siddharth123",
#         "email": "siddharth.gupta2@example.com",
#         "role": "doctor",
#         "experience": 10,
#         "speciality": "Orthopedics",
#         "department": "Orthopedics Department",
#         "department_id": "O303",
#         "hospital": "OrthoCare Hospital",
#         "available_slots": ["09:00 AM", "10:00 AM", "02:00 PM", "03:00 PM", "04:00 PM"],
#         "booked_slots": [],
#         "appointment_duration": 45,
#         "appointment_fee": 1200,
#     },
#     {
#         "full_name": "Dr. Meera Singh",
#         "age": 36,
#         "username": "meera_singh",
#         "password": "meera123",
#         "email": "meera.singh@example.com",
#         "role": "doctor",
#         "experience": 9,
#         "speciality": "Orthopedics",
#         "department": "Orthopedics Department",
#         "department_id": "O304",
#         "hospital": "Joint Health Center",
#         "available_slots": ["09:00 AM", "10:00 AM", "02:00 PM", "03:00 PM", "04:00 PM"],
#         "booked_slots": [],
#         "appointment_duration": 45,
#         "appointment_fee": 1000,
#     },
#     {
#       "full_name":
#       "Eva",
#       "age":
#       42,
#       "username":
#       "eva_martinez",
#       "password":
#       "eva456",
#       "email":
#       "eva.martinez@example.com",
#       "role":
#       "doctor",
#       "experience":
#       15,
#       "speciality":
#       "Dentistry",
#       "department":
#       "Dentistry Department",
#       "department_id":
#       "D103",
#       "hospital":
#       "Hospital 2",
#       "available_slots":
#       ["09:30 AM", "10:30 AM", "11:30 AM", "03:00 PM", "04:00 PM"],
#       "booked_slots": [],
#       "appointment_duration":
#       60,
#       "appointment_fee":
#       2000,
#     },
#   ]
#   doctors_collection.insert_many(doctors_data)
#   print("Doctors' details inserted successfully.")


# if __name__ == "__main__":
#   insert_doctors()
