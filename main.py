# # # import smtplib
# # #
# # # my_email = "yunoastha3@gmail.com"
# # # password = "kuvtetpqqxsdrwmr"
# # # connection = smtplib.SMTP("smtp.gmail.com")
# # # connection.starttls()
# # # connection.login(user=my_email, password=password)
# # # connection.sendmail(from_addr=my_email, to_addrs="endivaourmha@yahoo.com",
# # #                     msg="Hey".encode('utf-8'))
# # # connection.close()
# # # import datetime as dt
# # # now = dt.datetime.now()
# # # year = now.year
# # # month = now.month
# # # day_of_week = now.weekday()
# # # # print(day_of_week)
# # # # print(now, year)
# # # # print(type(year))
# # # date_of_birth = dt.datetime(year=2003, month=11, day=18)
# # # print(date_of_birth)
# #
# #
#Monday Motivation Project
# import smtplib
# import datetime as dt
# import random
#
# MY_EMAIL = "yunoastha3@gmail.com"
# MY_PASSWORD = "rgnjfotowrqpenoe"
#
# now = dt.datetime.now()
# weekday = now.weekday()
# if weekday == 1:
#     with open("../quotes.txt") as quote_file:
#         all_quotes = quote_file.readlines()
#         quote = random.choice(all_quotes)
#
#     print(quote)
#     with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#         connection.starttls()
#         connection.login(MY_EMAIL, MY_PASSWORD)
#         connection.sendmail(
#             from_addr=MY_EMAIL,
#             to_addrs="yunoastha3@gmail.com",
#             msg=f"Subject:Monday Motivation\n\n{quote}".encode('utf-8')
#         )
#
#
#
#

#
#
# ##################### Extra Hard Starting Project ######################
#
# # 1. Update the birthdays.csv
#
# # 2. Check if today matches a birthday in the birthdays.csv
#
# # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's
# # actual name from birthdays.csv
#
# # 4. Send the letter generated in step 3 to that person's email address.
#
from datetime import datetime
import random
import smtplib
import pandas

MY_EMAIL = "yunoastha3@gmail.com"
MY_PASSWORD = "rgnjfotowrqpenoe"
today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        print("OK")
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject: Happy Birthday!\n\n{contents}".encode("utf8")
                            )
