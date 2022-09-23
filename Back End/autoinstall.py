import mysql.connector as mysql #pip install mysql.connector
import os

def main(error=""):
    clear()
    print(error)
    print("Welcome to the backend installer for Ticket Auction Manager.\nThis will ask a few questions. As this is designed to create the necessary structure BEFORE an event, naming anything the same as previous db's and users will delete them.\nPress Ctrl+C to exit at any time.")
    orig_hostname = input("Enter the hostname of the server here (default = localhost): ")
    if orig_hostname == "":
        orig_hostname = "localhost"
    orig_username = input("Enter the hostname of the user with create and grant permissions here (default = root): ")
    if orig_username == "":
        orig_username = "root"
    orig_passwd = input("Enter that user's password here: ")
    try:
        conn = mysql.connect(host=orig_hostname, user=orig_username, password=orig_passwd)
    except:
        message = "Invalid host, user, or password. Please try again."
        main(message)
    print("Connection successful. It is safe to proceed.")
    cur = conn.cursor()
    new_database = input("Please insert the name of the new database you want to create: ")
    try:
        cur.execute(f"DROP DATABASE IF EXISTS {new_database}")
        cur.execute(f"CREATE DATABASE {new_database} DEFAULT CHARACTER SET 'utf8mb4'")
        cur.execute(f"USE {new_database}")
        cur.execute("CREATE TABLE regularticketst (ticketid INT PRIMARY KEY, firstname VARCHAR(50), lastname VARCHAR(50), phonenumber VARCHAR(50) DEFAULT \"NA\", preferstext SMALLINT DEFAULT 0)")
        cur.execute("CREATE TABLE specialtyticketst (ticketid INT PRIMARY KEY, firstname VARCHAR(50), lastname VARCHAR(50), phonenumber VARCHAR(50) DEFAULT \"NA\", preferstext SMALLINT DEFAULT 0)")
        cur.execute("INSERT INTO regularticketst (ticketid, firstname, lastname, phonenumber) VALUES (0, 'Winner Selected', 'No', '')")
        cur.execute("INSERT INTO specialtyticketst (ticketid, firstname, lastname, phonenumber) VALUES (0, 'Winner Selected', 'No', '')")
        conn.commit()
        cur.execute("CREATE TABLE regularbasketst (basketid INT PRIMARY KEY, description VARCHAR(255), donors VARCHAR(255), winningticket INT DEFAULT 0 REFERENCES regularticketst(ticketid))")
        cur.execute("CREATE TABLE specialtybasketst (basketid INT PRIMARY KEY, description VARCHAR(255), donors VARCHAR(255), winningticket INT DEFAULT 0 REFERENCES specialtyticketst(ticketid))")
        conn.commit()
        print("Database and tables created successfully. Let's move onto users.")
    except:
        message = "Database creation failed. Please try another user with database creation privileges."
        main(message)
    primaryuser = input("Enter the name of the primary user for the database (default = name of db): ")
    if primaryuser == "":
        primaryuser = new_database
    primarypasswd = input("Insert the password for the new primary user: ")
    try:
        cur.execute(f"DROP USER IF EXISTS '{primaryuser}'")
        cur.execute(f"CREATE USER '{primaryuser}'@'%' IDENTIFIED BY '{primarypasswd}'")
        cur.execute(f"GRANT ALL PRIVILEGES ON {new_database}.* TO '{primaryuser}'@'%' WITH GRANT OPTION")
        cur.execute("FLUSH PRIVILEGES")
    except:
        message = "User creation failed. Check privileges."
        main(message)
    print("Primary user created successfully.")
    conn.commit()
    while True:
        userprompt = input("Do you want to create auxiliary users (y or n): ")
        if userprompt == "n":
            quit()
        new_user = input("Enter the name of the new user (Entering nothing will exit): ")
        if new_user == "":
            quit()
        new_password = input("Enter the password for the new user: ")
        cur.execute(f"DROP USER IF EXISTS '{new_user}'")
        cur.execute(f"CREATE USER '{new_user}'@'%' IDENTIFIED BY '{new_password}'")
        cur.execute(f"GRANT ALL PRIVILEGES ON {new_database}.* TO '{new_user}'@'%'")
        cur.execute("FLUSH PRIVILEGES")
        conn.commit()

def clear():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

if __name__ == "__main__":
    main()