# imports psycopg2
import psycopg2
# imports Error from psycopg2
from psycopg2 import Error
# imports the get_connected function from our database.py file
from database import get_connected

###################################### TO DO #######################################
# write import statement to import create_customers and insert_customers from customers.py
# write import statement to import create_invoices and insert_invoices from invoices.py

from customers import create_customers, insert_customers
from invoices import create_invoices, insert_invoices

try:
    print("Connecting...")
    
    # connection to database
    connection = get_connected()

    # creates cursor
    cursor = connection.cursor()

    print("Connection successful.")

###################################### TO DO #######################################
    ############### CREATING TABLES AND INSERTING INFORMATION ###############

    print("Seeding database...")
    cursor.execute(create_customers)
    connection.commit()
    print("Customer table was created successfully.")

    cursor.execute(insert_customers)
    connection.commit()
    print("Customer information was inserted successfully.")

    cursor.execute(create_invoices)
    connection.commit()
    print("Invoices table was created successfully.")

    cursor.execute(insert_invoices)
    connection.commit()
    print("Invoices were inserted successfully")


# handles errors and prints them to the console - DO NOT ALTER OR DELETE

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL DB", error)

finally:
    if (connection):
        cursor.close()
        connection.close()
        print("DB connection is closed.")