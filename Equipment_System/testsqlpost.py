import datetime

checkin = "10/12/2019"
date_string = "10/02/2019"

print(datetime.datetime.now())
print(datetime.datetime.now() + datetime.timedelta(days=31))
print(datetime.date.today())


check_in_date = datetime.datetime.strptime(date_string, "%d/%m/%Y")
formatted_check_in_date = (check_in_date.strftime("%d/%m/%Y"))

print(check_in_date)
print(formatted_check_in_date)