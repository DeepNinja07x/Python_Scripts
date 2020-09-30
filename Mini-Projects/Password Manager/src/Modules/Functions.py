from Password_manager import * 
from Modules.Colours import *

def get_password(account):
    command = 'SELECT * from DETAILS WHERE ACCOUNT = "' + account + '"'
    cursor = conn.execute(command)
    for row in cursor:
        username = row[1]
        password = row[2]
    return [username, password]

def add_password(account, username, password):
    command = 'INSERT INTO DETAILS (ACCOUNT,USERNAME,PASSWORD) VALUES("'+account+'","'+username+'","'+password+'");'
    conn.execute(command)
    conn.commit()

def update_password(account, password):
    command = 'UPDATE DETAILS set PASSWORD = "' + password + '" where ACCOUNT = "' + account + '"'
    conn.execute(command)
    conn.commit()
    green("\n" + account + " password has been updated successfully.\n")

def delete_account(account):
    command = 'DELETE from DETAILS where ACCOUNT = "' + account + '"'
    conn.execute(command)
    conn.commit()
    green("\n"+account + " details have been deleted from the database successfully.\n")

def get_all():
    print()
    cursor.execute("SELECT * from DETAILS")
    data = cursor.fetchall()
    if len(data) == 0:
        red("No Data Present\n")
    else:
        for row in data:
            print("Account : ", row[0])
            print("Username : ", row[1])
            print("Password : ", row[2])
            print()

def check_details(account):
    cursor.execute("SELECT ACCOUNT from DETAILS where ACCOUNT = ?", (account,))
    data = cursor.fetchall()
    if len(data) == 0:
        return False
    else:
        return True

def destroy():
    cursor.execute('DELETE from DETAILS;',)
    print("\nDelete",cursor.rowcount,"records\n")
    conn.commit()