import pyodbc
import time
import datetime

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Database3.accdb;')
cursor = conn.cursor()

logged_in_user = "test"

def items_from_particular_user(user):
	query = "select * from Test_Equipment where Current_Holder=?"
	cursor.execute(query, user)
	if len(cursor.fetchall()) == 0: 
		print("you absolute hot dog, that user doesn't exist!")
	for row in cursor.fetchall():
		print(row[2])
		return row

	
def available_items():
    cursor.execute('select * from Test_Equipment where Availability=?', 'Available')
    for row in cursor.fetchall():
        print(row[2])
        #I can write random messages in your code whilst you're hard at work


def check_out(item, checkindate):
        """
        :func: scan item, assign user as current_holder, current date and time
        set check in date - maybe set a max of 31 days
        """


def check_in(item, user, notes):
	"""
	check that the user HAD the item, then ask them for the notes - need to add column to db
    to show item is/isnt broken... the update database to show item is available, no current_holder, 
	clear date fields and add new notes.
	"""
    #do I have the item - change item later to be item.name or something when we know what the scanner 
    # output is
    if item not in items_from_particular_user(user):
            print("You do not hold that item.")    
    notes = "test condition, it looks good"
    #update
    query = "UPDATE Test_Equipment SET Notes=?, Current_Holder='', Check_Out_Date = NULL, Due_Date = NULL"
    cursor.execute(query, notes)
    for row in cursor.fetchall():
        print(row)
    return row

def report_item(item):
        """
        dude someone broke the scope so please get someone to fix it xD
        """        
        

available_items()
users_items()
