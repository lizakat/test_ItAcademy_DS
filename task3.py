from datetime import datetime


def days_difference(date1, date2):
    try:
        date1_object = datetime.strptime(date1, '%d-%m-%Y')
        date2_object = datetime.strptime(date2, '%d-%m-%Y')
    except ValueError:
        print("Incorrect input. Use format DD-MM-YYYY.")
        return

    dif = date2_object - date1_object

    if dif.days < 0:
        abs_dif = abs(dif.days)
        print(abs_dif)
    else:
        print(dif.days)


date1 = "01-07-2023"
date2 = "11-07-2023"

days_difference(date1, date2)
