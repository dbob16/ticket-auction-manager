# Prerequisites
The following is required to run this database application.

* Microsoft Access 2007+
    * The latest x64 Access runtime works if you just need to use the compiled version.
* For MariaDB or MySQL Backend (coming soon), the following maybe required:
    * A computer or server running MariaDB or MySQL as a service
        * Root access or at the very least, db creation, user creation, and grant privileges
    * A Python interpreter on the computer or server, with access to an account with the permissions highlighted above (If you are to use the automated install script)
    * Permission to upload a .sql file if you'll opt to edit it manually

# Project Rundown
This is a public copy of the database application which I named 'Ticket Auction Manager' or 'TAM.' After much thought, I decided to release it for free, to the public, as it will benefit those working for non-profits and benefit 'chinese' auctions.

# Simple Directions
Unless you are a pro at opening, modifying, and maintaining Microsoft Access databases; to get started, just open the file named 'TAM_x64' in the Front End -> Compiled folders. It should open up if you have a compatible version of Microsoft Access installed.

After that the buttons are pretty self-explanatory. For the duplicate and copy/paste buttons to work, all fields in a row have to be filled in though.

If the file does not open, download and install the 64-bit Access 365 runtime at:

```
https://support.microsoft.com/en-us/office/download-and-install-microsoft-365-access-runtime-185c5a32-8ba9-491e-ac76-91cbe3ea09c9
```