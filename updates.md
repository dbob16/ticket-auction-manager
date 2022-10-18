# Updates (from newest to oldest)

## October 18th, 2022
Fixed reports:
* link to sequential reports on main menu
* Specialty sequential no longer links to regular ticket items

Fixed defaults for standalone version:
* Regular and Specialty basket tables now have a default of 0 on WinningTicket column allowing them to show up on the drawing form
* Regular and Specialty ticket tables now default 0 on the Text column so the check box is no longer boxed in by default

## September 23rd, 2022
Installer python script quickly hashed out and added. More to come.

## September 22nd, 2022
Wrote and added install.sql in the "Back End" folder, it needs to be changed in an editor and uploaded to an instance of MariaDB or MySQL. Then an ODBC data source named "tam" can be pointed to said instance using the MySQL Unicode ODBC driver.

Added copies of the database which will automatically connect to a named data source "tam", they are suffixed with "ODBC_MYSQL"

## September 21st, 2022
Added repo to GitHub, from some of my source files I keep privately.

Wrote new documentation under readme.md.