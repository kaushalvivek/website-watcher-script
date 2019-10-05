import requests
import os
import sys
import smtplib

#################################################
# Login details of any *gmail* account
bot_mail = ''
password = ''
target_mail = ''
#################################################

# Config - don't touch
URL = sys.argv[1]
TEMP_FILE = "/tmp/watcher_cache.txt"
try:
    TOLERANCE = int(sys.argv[2])  # in different characters
except Exception as e:
    print('Taking a default tolerance of 100')
    TOLERANCE = 100

# Mail -- modified
def mail(URL):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(bot_mail, password)
    SUBJECT = "New Changes on "+ URL
    TEXT = "Hi Human, there are new changes on "+URL+" Click on the link to checkout.\n Cheers!"
    msg = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    server.sendmail(bot_mail, target_mail, msg)
    server.quit()

# Read length of old web page version
try:
    f = open(TEMP_FILE, 'r')
    len1 = len(f.read())
    f.close()
except:
    len1 = 0

# Read length of current web page version
r = requests.get(URL)
if r.status_code is not 200:
    print('Could not fetch %s.' % URL)
    len2 = 0
else:
    len2 = len(r.text)

# Write new version to file
try:
    f = open(TEMP_FILE, 'w+')
    f.write(r.text)
    f.close()
except Exception as e:
    print('Could not open file %s: %s' % (TEMP_FILE, e))

diff = abs(len2 - len1)
print(diff)
if diff > TOLERANCE:
    mail(URL)
    print("Mail Sent")
else:
    print("No change")