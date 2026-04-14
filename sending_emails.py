import smtplib
from email.mime.text import MIMEText

body = "This is a test email.How are you"
msg = MIMEText(body)

msg['From'] = "viveksingh031023@gmail.com"
msg['To'] = "viveksingh102303@gmail.com"
msg['Subject'] = "Hello"

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

server.login("viveksingh031023@gmail.com", "ohkyxyzqrosrkzsf")
server.sendmail(msg['From'], [msg['To']], msg.as_string())
print("EMail is sent to viveksingh102303@gmail.com successfully.")
server.quit()