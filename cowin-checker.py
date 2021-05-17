import os
import json
import requests
from datetime import datetime, timedelta
import time
import logging

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

emails = {
    307: ["kanish671@gmail.com"],
    505: [],
    506: [],
    169: [],
    773: []
}

bbmp = 294
blr_urban = 265
gurgaon = 188
mumbai = 395
varanasi = 696
rampur = 683
ernakulam = 307
jaipur_1 = 505
jaipur_2 = 506
jamnagar_1 = 169
jamnagar_corp = 773

sleep_duration = 300
today = datetime.today()
date1 = today.strftime("%d-%m-%Y")
date2 = (today + timedelta(days=7)).strftime("%d-%m-%Y")
date3 = (today + timedelta(days=14)).strftime("%d-%m-%Y")
EMAIL = os.environ['EMAIL']
PASSWORD = os.environ['PASSWORD']

def send_email(email, body):
    mail_content = body
    #The mail addresses and password
    sender_address = EMAIL
    sender_pass = PASSWORD
    receiver_address = email
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Vaccine Availability for 18+ | Centre Name, Pincode, Date, Availability'
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    logging.info('Mail Sent')

def get_available_centres(centre, date):
    result = []
    response = requests.get("https://cdn-api.co-vin.in/api/v2/appointment/sessions/calendarByDistrict?district_id={0}&date={1}"
                        .format(centre, date))
    logging.info(response)
    try:
        resp_dict = json.loads(response.text)
    except:
        logging.info("failed for centre: " + str(centre))
        return result

    logging.info("success for centre: " + str(centre))
    for item in resp_dict['centers']:
        centre_name = item['name']
        pincode = item['pincode']
        sessions = item['sessions']
        for elem in sessions:
            age_limit = int(elem['min_age_limit'])
            available_capacity = int(elem['available_capacity'])
            date2 = elem['date']
            if age_limit == 18 and available_capacity > 1:
                result.append([centre_name, str(pincode), date2, str(available_capacity)])
                logging.info(centre_name, pincode, date2, available_capacity)
    body = ""
    for item in result:
        body += ("-----".join(item) + "\\n")
    if len(result) > 0:
        email_list = emails[centre]
        for email in email_list:
            send_email(email, body)
    return result

def main():
    logging.basicConfig(filename='logs-cowin-checker.log', format='%(levelname)s:\t[%(asctime)s]\t%(message)s',
	datefmt='%d/%m/%Y %I:%M:%S %p', level=logging.INFO)
    while(1):
        for date in [date1]:
            for centre in [ernakulam]:
                get_available_centres(centre, date)
        time.sleep(sleep_duration)

if __name__ == '__main__':
    main()
