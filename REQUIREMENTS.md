# System Requirements

Below are the system requirements for the different parts of the project.

## Frontend

This is the part which runs on each computer that will be used to enter data or generate reports. The requirements for this part are below:

* CPU: 2GHz Dual-Core or better
* RAM: 8GB or more
* Storage: 10GB Available (Standalone), 2GB Available (Connected)
* Operating System: Microsoft Windows 10 or 11
* Prerequisites:
    * Microsoft Office 2013+/365 ProPlus or Microsoft Access 2013+/365 Runtime (Only works with release versions) [Download from Microsoft](https://support.microsoft.com/en-gb/office/download-and-install-microsoft-365-access-runtime-185c5a32-8ba9-491e-ac76-91cbe3ea09c9)
    * MySQL ODBC Driver with 'tam' DSN created in ODBC Data Sources.
        * ODBC Drivers [available here](https://dev.mysql.com/downloads/connector/odbc/)

## Backend

The backend is the part which stores the data (Connected version only) and networks multiple frontends together:

* CPU: 2GHz Dual-Core or better
* RAM: 4GB or more (Linux), 8GB or more (Windows)
* Storage: 10GB Available
* Operating System: Linux (Debian recommended) or Windows 10 or 11
* Prerequisites:
    * MariaDB Server with access to a root-level account
        * Windows download [is here](https://mariadb.org/download/?t=mariadb&p=mariadb&r=11.1.2&os=windows&cpu=x86_64&pkg=msi&m=acorn)
        * Linux: Use the package manager for your distro to install and setup mariadb or mariadb-server
            * For Debian: `sudo apt install mariadb-server` & `sudo mysql_secure_installation`
            * See video "How to setup connected version" in README.md to see how to install it
    * Port 3306 open in Firewall
