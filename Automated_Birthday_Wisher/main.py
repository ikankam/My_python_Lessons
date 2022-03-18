import random

import pandas
import datetime as dt
import smtplib

# Getting today's day and month
now = dt.datetime.now()
birth_day = now.day
birth_month = now.month

# Reading the file to get the individual info. Then checking if today matches any date in data.
data = pandas.read_csv("birthdays.csv")
for index, row in data.iterrows():
    if birth_day == row['day'] and birth_month == row['month']:
        choice = random.randint(0, 2)
        print(choice)

        # Getting the letter templates
        if choice == 0:
            with open("letter_templates/letter_1.txt") as letter_1:
                letter1 = letter_1.read()
                print(letter1)
                new_letter = letter1.replace("[NAME]", row['name'])
                print(new_letter)
        elif choice == 1:
            with open("letter_templates/letter_2.txt") as letter_2:
                letter2 = letter_2.read()
                new_letter = letter2.replace("[NAME]", row['name'])
                print(new_letter)
        else:
            with open("letter_templates/letter_3.txt") as letter_3:
                letter3 = letter_3.read()
                new_letter = letter3.replace("[NAME]", row['name'])
                print(new_letter)

# 4. Send the letter generated in step 3 to that person's email address.
            email = "my_email@gmail.com"
            password = "your_password_here"
            with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
                connection.starttls()
                connection.login(user=email, password=password)
                connection.sendmail(from_addr=email, to_addrs="recipient_email@yahoo.com",
                                    msg=f"Subject:Happy Birthday! :)\n\n {new_letter}")
