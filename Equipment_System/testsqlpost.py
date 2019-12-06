import datetime

checkin = "10/12/2019"
date_string = "10/02/2019"

check_out_date = datetime.datetime.now().strftime("%d/%m/%Y")
print(check_out_date)
