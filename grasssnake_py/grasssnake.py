#FOR SENDING EMAIL
import smtplib
import email
import imghdr
def sendEmail(toEmail, fromEmail, emailPassword, textMessage, attachPicture = False, pictureName = None):   

    msg = email.message.EmailMessage()
    msg.set_content(textMessage)
    msg['Subject'] = "Busted By Grass Snake"
    msg['To'] = toEmail
    msg['From'] = fromEmail
    msg['Text'] = textMessage

    if attachPicture:
        with open(pictureName + '.png', 'rb') as fp:
            img_data = fp.read()
        msg.add_attachment(img_data, maintype='image', subtype=imghdr.what(None, img_data))

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as s:
        s.login(fromEmail, emailPassword)
        s.send_message(msg)

#FOR CAMERA ACCESS
import cv2
def takePicture():
    cap = cv2.cv2.VideoCapture(0)
    _ , frame = cap.read()
    cv2.cv2.imwrite('busted.png',frame)
    cv2.cv2.destroyAllWindows()
    cap.release()

#MAIN LOOP
import win32gui
import re
import time

startTime = time.time()

with open('info.txt', 'r') as info:
    userinfo = re.findall(r'(?: = ([\w\S ]+))', info.read())

foldername = userinfo[0]
fromEmail = userinfo[1]
toEmail = userinfo[2]
emailPassword = userinfo[3]
#Making hours to seconds
TTL = float(userinfo[4]) * 3600 
terminatedIfCatched = userinfo[5]
secondsBetweenSearches = userinfo[6]
useCamera = userinfo[7]
pictureName = userinfo[8]
message = userinfo[9]

#will loop until the user-specifed time has passed
while time.time() - startTime <= TTL:
    window = win32gui.GetWindowText(win32gui.GetForegroundWindow())
    if window == foldername:
        if useCamera in ["True", "true", "1"]:
            takePicture()
            sendEmail(toEmail, fromEmail, emailPassword, message, True, pictureName)
        else:
            sendEmail(toEmail, fromEmail, emailPassword, message)
        if terminatedIfCatched in ["True", "true", "1"]:
            break
    time.sleep(float(secondsBetweenSearches))