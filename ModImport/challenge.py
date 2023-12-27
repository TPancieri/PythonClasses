# Create a program that allows a user to choose one of
# up to 9 time zones from a menu. You can choose any
# zones you want from the all_timezones list.
#
# The program will then display the time in that timezone, as
# well as local time and UTC time.
#
# Entering 0 as the choice will quit the program.
#
# Display the dates and times in a format suitable for the
# user of your program to understand, and include the
# timezone name when displaying the chosen time.

from datetime import datetime as dt, timezone
import zoneinfo

utc_now = dt.now(timezone.utc)

chosen_tz = None
user_in = "-"
while user_in != "0":
    possible_tz = {'1': 'Europe/Dublin',
                   '2': 'Australia/Sydney',
                   '3': 'Europe/Dublin',
                   '4': 'Pacific/Fiji',
                   '5': 'Asia/Dubai',
                   '6': 'Brazil/Acre',
                   '7': 'Europe/Kiev',
                   '8': 'Japan',
                   '9': 'Asia/Brunei',
                   }
    if user_in in possible_tz:
        chosen_tz = possible_tz[user_in]
        print(chosen_tz)
        tz_choice = zoneinfo.ZoneInfo(chosen_tz)
        chosen = utc_now.astimezone(tz=tz_choice)
        print(chosen.strftime("\t %Y-%m-%d \n\t %H:%M:%S"), "\n\t", chosen.tzname())
    else:
        print("Please choose an available time zone: \t")
        for k, i in possible_tz.items():
            print(k, i, sep=" : ")
    user_in = input(" >  ")
