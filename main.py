import datetime

import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import pywhatkit

# df = pd.DataFrame(
#     {
#         "Monday": [
#             "09 - 10 : No class in this time",
#             "10 - 11 : CSE42D (801) L",
#             "11 - 12 : CSE33D (307) P",
#             "12 - 01 : CSE33D (307) P",
#             "01 - 02 : LUNCH BREAK",
#             "02 - 03 : CSE38D (807) L",
#             "03 - 04 : CSE50D (701A) L",
#             "04 - 05 : No class in this time"
#         ],
#         "Tuesday": [
#             "09 - 10 : CSE39D (307) P",
#             "10 - 11 : CSE39D (307) P",
#             "11 - 12 : CSE38D (809) L",
#             "12 - 01 : CSE32D (809) L",
#             "01 - 02 : LUNCH BREAK",
#             "02 - 03 : CSE43D (305) P",
#             "03 - 04 : CSE43D (305) P",
#             "04 - 05 : CSE43D (305) P"
#         ],
#         "Wednesday": [
#             "09 - 10 : No class in this time",
#             "10 - 11 : CSE42D (801) L",
#             "11 - 12 : CSE49D (310) P",
#             "12 - 01 : CSE49D (310) P",
#             "01 - 02 : LUNCH BREAK",
#             "02 - 03 : CSE46D (809) L",
#             "03 - 04 : CSE38D (809) L",
#             "04 - 05 : CSE48D (809) L"
#         ],
#         "Thursday": [
#             "09 - 10 : CSE33D (305) P",
#             "10 - 11 : CSE33D (305) P",
#             "11 - 12 : CSE42D (801) L",
#             "12 - 01 : CSE32D (801) L",
#             "01 - 02 : LUNCH BREAK",
#             "02 - 03 : CSE48D (809) L",
#             "03 - 04 : CSE46D (809) L",
#             "04 - 05 : CSE50D (809) L"
#         ],
#         "Friday": [
#             "09 - 10 : CSE49D (307) P",
#             "10 - 11 : CSE49D (307) P",
#             "11 - 12 : CSE48D (809) L",
#             "12 - 01 : CSE46D (809) L",
#             "01 - 02 : LUNCH BREAK",
#             "02 - 03 : CSE32D (305) L",
#             "03 - 04 : No class in this time",
#             "04 - 05 : No class in this time"
#         ],
#     }
# )
# df.to_csv("Timetable.csv", index=False)
df = pd.read_csv("Timetable.csv")
current_date = datetime.datetime.now()
week_day = current_date.weekday()
today_time_table = ""
current_hour = current_date.hour
current_time_table = ""
if week_day != 6:
    today_time_table = (df.iloc[:, week_day])
    if current_hour == 8:
        current_time_table = today_time_table
    elif current_hour == 9:
        current_time_table = today_time_table.iloc[0]
    elif current_hour == 10:
        current_time_table = today_time_table.iloc[1]
    elif current_hour == 11:
        current_time_table = today_time_table.iloc[2]
    elif current_hour == 12:
        current_time_table = today_time_table.iloc[3]
    elif current_hour == 13:
        current_time_table = today_time_table.iloc[4]
    elif current_hour == 14:
        current_time_table = today_time_table.iloc[5]
    elif current_hour == 15:
        current_time_table = today_time_table.iloc[6]
    elif current_hour == 16:
        current_time_table = today_time_table.iloc[7]
        print(current_time_table)
    else:
        current_time_table = "Your Academic hour is OVER, You can gain new skills now..."

elif week_day == 6:
    today_time_table = "Today is Sunday Enjoy Your Life..."

# sent email to user
# Email credentials
email_address = "deepakjgrt99@gmail.com"
password = "eljlasisljrvlxkx"

# Recipient email address
recipient_email = "deepakjgrt@example.com"

# Create message
message = MIMEMultipart()
message["From"] = email_address
message["To"] = recipient_email
message["Subject"] = "ToDays Time Table"

body = current_time_table

message.attach(MIMEText(body, "plain"))

# Connect to Gmail's SMTP server
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(email_address, password)
    server.send_message(message)
message = f"Today/current time table \n {current_time_table}"
time_min = 0
# for rec in recipient:
pywhatkit.sendwhatmsg_to_group("Jnf5l7bWE89FIkZAQ75q28",
                               message,
                               current_hour, time_min)
# time_min += 1

print("Email sent successfully!")
