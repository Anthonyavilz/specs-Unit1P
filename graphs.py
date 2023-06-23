############################# TO DO #####################################

# write import statement for psycopg2

# write import statement to import Error from psycopg2

# import the get_connected function from your database.py file

# import matplotlib.pyplot as plt
import psycopg2
from psycopg2 import Error
from database import get_connected
import matplotlib.pyplot as plt

try:
    # connection to database
    connection = get_connected()

    # creates cursor
    cursor = connection.cursor()

############################# TO DO #####################################

    product_revenue_query = """
        SELECT product_category,
        SUM (unit_price*quantity)
        FROM invoices
        GROUP BY product_category
        ORDER BY SUM DESC
    """

    def get_revenue():
        with connection:
            with cursor:
                cursor.execute(product_revenue_query)
                return cursor.fetchall()
        
    product_revenue = get_revenue()

    product_categories = []
    total_revenue = []
    # count = 0
    index = 0

    for number in product_revenue:
        product_categories.append(product_revenue[index][0])
        total_revenue.append(int(product_revenue[index][1]))
        index += 1

    # while count < (len(product_revenue)):
    #     product_categories.append(product_revenue[index][0])
    #     total_revenue.append(int(product_revenue[index][1]))

    #     count += 1

    def create_bar_chart():
        figure = plt.figure()
        data = total_revenue
        labels = product_categories

        plt.xticks(range(len(labels)), labels, rotation=90)
        plt.xlabel('Product Category')
        plt.ylabel('Revenue (USD)')
        plt.title('Product Revenue by Category')

        plt.bar(labels, data)

        return figure
    
    create_bar_chart()
    plt.show()

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL DB", error)

finally:
    if (connection):
        cursor.close()
        connection.close()
        print("DB connection is closed.")