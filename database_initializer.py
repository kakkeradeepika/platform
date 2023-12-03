# database_initializer.py
from database_connector import connection
import config

def db_init():
    conn, c = connection()
    with conn:
        c.execute(
            """
            CREATE TABLE IF NOT EXISTS patient_record (
                id VARCHAR(255) PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                age INT NOT NULL,
                gender VARCHAR(255) NOT NULL,
                date_of_birth VARCHAR(255) NOT NULL,
                blood_group VARCHAR(255) NOT NULL,
                contact_number_1 VARCHAR(255) NOT NULL,
                contact_number_2 VARCHAR(255),
                aadhar_or_voter_id VARCHAR(255) NOT NULL UNIQUE,
                weight INT NOT NULL,
                height INT NOT NULL,
                address TEXT NOT NULL,
                city VARCHAR(255) NOT NULL,
                state VARCHAR(255) NOT NULL,
                pin_code VARCHAR(255) NOT NULL,
                next_of_kin_name VARCHAR(255) NOT NULL,
                next_of_kin_relation_to_patient VARCHAR(255) NOT NULL,
                next_of_kin_contact_number VARCHAR(255) NOT NULL,
                email_id VARCHAR(255),
                date_of_registration VARCHAR(255) NOT NULL,
                time_of_registration VARCHAR(255) NOT NULL
            );
            """
        )
    with conn:
        c.execute(
            """
            CREATE TABLE IF NOT EXISTS doctor_record (
                id VARCHAR(255) PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                age INT NOT NULL,
                gender VARCHAR(255) NOT NULL,
                date_of_birth VARCHAR(255) NOT NULL,
                blood_group VARCHAR(255) NOT NULL,
                department_id VARCHAR(255) NOT NULL,
                department_name VARCHAR(255) NOT NULL,
                contact_number_1 VARCHAR(255) NOT NULL,
                contact_number_2 VARCHAR(255),
                aadhar_or_voter_id VARCHAR(255) NOT NULL UNIQUE,
                email_id VARCHAR(255) NOT NULL UNIQUE,
                qualification VARCHAR(255) NOT NULL,
                specialisation VARCHAR(255) NOT NULL,
                years_of_experience INT NOT NULL,
                address TEXT NOT NULL,
                city VARCHAR(255) NOT NULL,
                state VARCHAR(255) NOT NULL,
                pin_code VARCHAR(255) NOT NULL,
                FOREIGN KEY (department_id) REFERENCES department_record(id)
                ON UPDATE CASCADE
                ON DELETE RESTRICT
            );
            """
        )
    with conn:
        c.execute(
            """
            CREATE TABLE IF NOT EXISTS department_record (
                id VARCHAR(255) PRIMARY KEY,
                name VARCHAR(255) NOT NULL UNIQUE,
                description TEXT NOT NULL,
                contact_number_1 VARCHAR(255) NOT NULL,
                contact_number_2 VARCHAR(255),
                address TEXT NOT NULL,
                email_id VARCHAR(255) NOT NULL UNIQUE
            );
            """
        )
    with conn:
        c.execute(
            """
            CREATE TABLE IF NOT EXISTS prescription_record (
                id VARCHAR(255) PRIMARY KEY,
                patient_id VARCHAR(255) NOT NULL,
                patient_name VARCHAR(255) NOT NULL,
                doctor_id VARCHAR(255) NOT NULL,
                doctor_name VARCHAR(255) NOT NULL,
                diagnosis TEXT NOT NULL,
                comments TEXT,
                medicine_1_name VARCHAR(255) NOT NULL,
                medicine_1_dosage_description TEXT NOT NULL,
                medicine_2_name VARCHAR(255),
                medicine_2_dosage_description TEXT,
                medicine_3_name VARCHAR(255),
                medicine_3_dosage_description TEXT,
                FOREIGN KEY (patient_id) REFERENCES patient_record(id)
                ON UPDATE CASCADE
                ON DELETE RESTRICT,
                FOREIGN KEY (doctor_id) REFERENCES doctor_record(id)
                ON UPDATE CASCADE
                ON DELETE RESTRICT
            );
            """
        )
    with conn:
        c.execute(
            """
            CREATE TABLE IF NOT EXISTS medical_test_record (
                id VARCHAR(255) PRIMARY KEY,
                test_name VARCHAR(255) NOT NULL,
                patient_id VARCHAR(255) NOT NULL,
                patient_name VARCHAR(255) NOT NULL,
                doctor_id VARCHAR(255) NOT NULL,
                doctor_name VARCHAR(255) NOT NULL,
                medical_lab_scientist_id VARCHAR(255) NOT NULL,
                test_date_time VARCHAR(255) NOT NULL,
                result_date_time VARCHAR(255) NOT NULL,
                result_and_diagnosis TEXT,
                description TEXT,
                comments TEXT,
                cost INT NOT NULL,
                FOREIGN KEY (patient_id) REFERENCES patient_record(id)
                ON UPDATE CASCADE
                ON DELETE RESTRICT,
                FOREIGN KEY (doctor_id) REFERENCES doctor_record(id)
                ON UPDATE CASCADE
                ON DELETE RESTRICT
            );
            """
        )
    conn.close()
