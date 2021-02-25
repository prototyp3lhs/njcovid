from selenium import webdriver
from datetime import datetime
import time
import smtplib
import os

URL = "https://curogram.com/registrations/5fe2fe643b4a850044b0b3b1"

# ADD YOUR EMAIL AND PASSWORD HERE:
MY_EMAIL_LOGIN = "myemail@gmail.com"
MY_EMAIL_PASSWORD = "myemailpassword"

# EMAILS OF INDIVIDUALS YOU'D LIKE TO ALERT
email_list = [
    "email1@gmail.com",
    "email2@gmail.com",
]

# DOWNLOAD CHROMEDRIVER AND PLACE IN SAME DIRECTORY
driver = webdriver.Chrome("chromedriver.exe")

while True:
    try:
        driver.get(URL)
        time.sleep(3)
    except Exception as e:
        print("Connection issue" + str(e))
        continue
    website = driver.current_url.find('blocked')
    if website == 60:
        now = datetime.now().strftime("%c")
        print(f"Current Time = {now}\n")

        time.sleep(120)
    else:
        now = datetime.now().strftime("%c")
        print(f"COVID SHOT AVAILABLE! --- Current Time = {now}\n")
        # mac voice command
        os.system('say "covid shot available."')

    try:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL_LOGIN, password=MY_EMAIL_PASSWORD)
            for email in email_list:
                connection.sendmail(
                    from_addr=MY_EMAIL_LOGIN,
                    to_addrs=email,
                    msg=f"Subject:NJ COVID SHOT AVAILABLE\n\n'COVID SHOT AVAILABLE, sign up using the following link: {URL}".encode("UTF-8")
                )
    except Exception as ex:
        print("Could not send email" + str(ex))
