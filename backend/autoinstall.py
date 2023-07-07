import mysql.connector as m
from getpass import getpass

def main():
    connstr = connect()

    cnx = m.connect(host=connstr['host'], port=connstr['port'], user=connstr['user'], password=connstr['password'])
    cn = cnx.cursor()

    new_db = input("Please enter name of new database: [default = tam] ")
    if new_db == "":
        new_db = "tam"
    cn.execute(f"DROP DATABASE IF EXISTS `{new_db}`")
    cnx.commit()
    cn.execute(f"CREATE DATABASE IF NOT EXISTS `{new_db}` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */")
    cnx.commit()
    cn.execute(f"USE `{new_db}`")

    cn.execute("""CREATE TABLE IF NOT EXISTS `t_regulartickets` (
    `TicketID` int(11) NOT NULL DEFAULT 0,
    `FirstName` varchar(50) DEFAULT NULL,
    `LastName` varchar(50) DEFAULT NULL,
    `PhoneNumber` varchar(50) DEFAULT NULL,
    `PrefersText` int(11) NOT NULL DEFAULT 0,
    PRIMARY KEY (`TicketID`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci""")
    cn.execute("INSERT INTO `t_regulartickets` (TicketID, FirstName, LastName, PhoneNumber) VALUES (0, 'No', 'Winner', 'Selected')")
    cnx.commit()
    cn.execute("""CREATE TABLE IF NOT EXISTS `t_specialtytickets` (
    `TicketID` int(11) NOT NULL DEFAULT 0,
    `FirstName` varchar(50) DEFAULT NULL,
    `LastName` varchar(50) DEFAULT NULL,
    `PhoneNumber` varchar(50) DEFAULT NULL,
    `PrefersText` int(11) NOT NULL DEFAULT 0,
    PRIMARY KEY (`TicketID`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci""")
    cn.execute("INSERT INTO `t_specialtytickets` (TicketID, FirstName, LastName, PhoneNumber) VALUES (0, 'No', 'Winner', 'Selected')")
    cnx.commit()
    cn.execute("""CREATE TABLE IF NOT EXISTS `t_regularbaskets` (
    `BasketID` int(11) NOT NULL,
    `Description` varchar(255) DEFAULT '',
    `Donors` varchar(255) DEFAULT '',
    `WinningTicket` int(11) NOT NULL DEFAULT 0,
    PRIMARY KEY (`BasketID`),
    KEY `regularrelation` (`WinningTicket`),
    CONSTRAINT `regularrelation` FOREIGN KEY (`WinningTicket`) REFERENCES `t_regulartickets` (`TicketID`) ON DELETE NO ACTION ON UPDATE NO ACTION
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci""")
    cn.execute("""CREATE TABLE IF NOT EXISTS `t_specialtybaskets` (
    `BasketID` int(11) NOT NULL,
    `Description` varchar(255) DEFAULT '',
    `Donors` varchar(255) DEFAULT '',
    `WinningTicket` int(11) NOT NULL DEFAULT 0,
    PRIMARY KEY (`BasketID`) USING BTREE,
    KEY `specialtyrelation` (`WinningTicket`),
    CONSTRAINT `specialtyrelation` FOREIGN KEY (`WinningTicket`) REFERENCES `t_specialtytickets` (`TicketID`) ON DELETE NO ACTION ON UPDATE NO ACTION
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci""")
    cnx.commit()
    print(f"Database {new_db} and its tables created successfully.")

    new_user = input(f"Please enter username for new user: [default = {new_db}] ")
    if new_user == "":
        new_user = new_db
    new_passwd = getpass("Please enter password for new user: ")

    cn.execute(f"CREATE USER '{new_user}'@'%' IDENTIFIED BY '{new_passwd}'")
    cn.execute(f"GRANT ALL PRIVILEGES ON `{new_db}`.* TO '{new_user}'@'%' WITH GRANT OPTION")
    cnx.commit()
    cn.execute("FLUSH PRIVILEGES")



def connect():
    hostnameip = input("Please enter hostname/ip: [default = localhost]")
    if hostnameip == "":
        hostnameip = "localhost"
    portnum = input("Please enter port number: [default = 3306] ")
    if portnum == "":
        portnum = "3306"
    try:
        portnum = int(portnum)
    except:
        print("Try entering a number or nothing (just press enter) for port next time.")
    username = input("Please enter username: [default = root] ")
    if username == "":
        username = "root"
    password = getpass("Please enter password: ")
    cnx = m.connect(host=hostnameip, port=portnum, user=username, password=password)
    cn = cnx.cursor()

    cn.execute("SHOW GRANTS")
    result = cn.fetchone()

    score = 0
    if result[0].startswith("GRANT ALL PRIVILEGES ON *.* TO"):
        score += 1
    if result[0].endswith("WITH GRANT OPTION"):
        score += 1
    
    if score == 2:
        print("Permissions good, continuing.")
    else:
        print("Permissions not good, retry.")

    return {"host": hostnameip, "port": portnum, "user": username, "password": password}

if __name__ == "__main__":
    main()