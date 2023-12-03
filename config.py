# configuration file containing confidential credentials
# user authentication password is used to login to the application
# edit mode password is required to add, delete or update any patient, doctor or department record 
# doctor/medical lab scientist (MLS) access code is given only to the doctors and MLSs, using which they can add, delete or update any prescription and/or medical test record

# password = '1234'                               # e.g. password = '1234'
# database_name = 'healthCare'                                 # e.g. database_name = 'database_1A'
# edit_mode_password = 'allow_edit'                               # e.g. edit_mode_password = 'allow_edit'
# dr_mls_access_code = 'access_auth'      # e.g. dr_mls_access_code = 'access_auth'




# # config.py

# # SQLite Configuration
# database_name = "healthCare"

# # MySQL Configuration
# mysql_host = "localhost/3306"
# mysql_user = "admin"
# mysql_password = "1234"
# mysql_database = "healthcare_db"
import mysql.connector

# Replace these values with your actual database credentials
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "Racha@1630",
    "database": "healthcare_db",
    "port": 3306,
}

# Create a connection
connection = mysql.connector.connect(**db_config)

# Create a cursor
cursor = connection.cursor()

# Your SQL queries go here

# Close the cursor and connection when done
cursor.close()
connection.close()