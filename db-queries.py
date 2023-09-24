import psycopg2
import datetime

try:

    # Get the current date and time
    current_datetime = datetime.datetime.now()

    print("trying to connect to postgresql...")
    connection = psycopg2.connect(
        dbname='pagila',
        user='postgres',
        password='password',
        host='localhost',
        port='5432'
    )
    print("Connected to the database")
    cursor = connection.cursor()

    table_name  = "actor"
    
    ## Execute the SQL query
    cursor.execute(f"""
        SELECT COUNT(*) as total_count
        FROM {table_name};
    """)

    ## Fetch and print the results
    result = cursor.fetchone()
    total_count = result[0]
    print(f"Total Count of element in {table_name} table: {total_count}")

    ## Excecute select query   
    cursor.execute(f"SELECT * FROM {table_name} limit 10")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    ## Execute the query to retrieve column names
    table_name = 'actor'  # Replace with your table name
    cursor.execute("""
        SELECT column_name
        FROM information_schema.columns
        WHERE table_name = %s;
    """, (table_name,))

    # Fetch and print the column names
    column_names = [row[0] for row in cursor.fetchall()]
    print("Column Names:", column_names)
    
    column1 = "actor_id"
    column2 = "first_name"
    column3 = "last_name"
    column4 = "last_update"
    ## Define the SQL query to insert values
    insert_query = f"""
        INSERT INTO actor ({column1}, {column2}, {column3}, {column4})
        VALUES (%s, %s, %s, %s);
    """
    # Define the values to be inserted
    # Convert it to a string in a specific format (optional)
    timestamp_str = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    values_to_insert = ('202', 'Sonia', 'Stella', timestamp_str)  # Replace with your values
    cursor.execute(insert_query, values_to_insert)  # Execute the INSERT statement with the values
    connection.commit() # Commit the transaction (save changes)
    print(f"Data : {values_to_insert} inserted successfully")

    cursor.close()
    connection.close()
    print("Connection closed")
except psycopg2.Error as e:
    print("Error:", e)
