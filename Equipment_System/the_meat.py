import pyodbc
import datetime

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\temp\Database31.accdb;')
cursor = conn.cursor()

logged_in_user = "Harry Fiske"
notes = "test condition, it looks good"

# :TODO: https://docs.python.org/2/library/logging.html
#   https://jackworthen.com/2018/03/19/creating-a-log-table-to-track-changes-to-database-objects-in-sql-server/

def items_from_particular_user(user):
    query = "select * from Test_Equipment where Current_Holder=?"
    stored_ans = cursor.execute(query, user).fetchall()
    if len(stored_ans) != 0:
        # for row in stored_ans:
        #    print(row[2])
        # return row
        print(stored_ans[0][2])
    else:
        print("you absolute hot dog, that user doesn't exist!")


def all_items():
    query = 'select * from Test_Equipment'
    result = cursor.execute(query).fetchall()
    #    for row in result:
    #        return row
    print(result)
    return result


def available_items():
    cursor.execute('select * from Test_Equipment where Availability=?', 'Available')
    for row in cursor.fetchall():
        print(row[2])


def check_out(item, date_string):
    """
    :func: scan item, assign user as current_holder, current date and time
    set check in date - maybe set a max of 31 days. accepts date in format  "dd/mm/yyyy"
    """
    check_out_date = datetime.datetime.now().strftime("%d/%m/%Y")
    check_in_date = datetime.datetime.strptime(date_string, "%d/%m/%Y")
    formatted_check_in_date = (check_in_date.strftime("%d/%m/%Y"))
    if check_in_date < (datetime.datetime.now() + datetime.timedelta(days=32)):
        print("Check-in date will be: " + str(datetime.date.today() + datetime.timedelta(days=32)))
        query = "UPDATE Test_Equipment SET Current_Holder=?, Check_Out_Date =?, Due_Date =?, Availability ='Unavailable' WHERE Item_Name=?"
        cursor.execute(query, logged_in_user, check_out_date, formatted_check_in_date, item)
        conn.commit()
    else:
        print("You can't borrow an item for that long!")


# TODO: check if items are overdue, also which items are overdue overall

def check_in(item, user, notes):
    #    TODO: change item to item code when moving from development
    """
    check that the user HAD the item, then ask them for the notes - need to add column to db
    to show item is/isnt broken... the update database to show item is available, no current_holder, 
    clear date fields and add new notes.
    """
    # do I have the item - change item later to be item.name or something when we know what the scanner
    # output is
    if item in items_from_particular_user(user):
        # update
        query = "UPDATE Test_Equipment SET Notes=?, Current_Holder='', Check_Out_Date = NULL, Due_Date = NULL WHERE Current_Holder=? AND Item_Code=?"
        cursor.execute(query, notes, user, item)
        for row in cursor.fetchall():
            print(row)
        return row
    else:
        print("You do not hold that item.")


def report_item(item):
    """
        dude someone broke the scope so please get someone to fix it xD
        """


#check_out("item3", "05/01/2020")
# all_items()
available_items()
# items_from_particular_user("test")
