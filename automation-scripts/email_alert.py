import smtplib
from email.mime.text import MIMEText

text = "This is an automated alert."

msg = MIMEText(text)
msg["Subject"] = "Auto Alert"
msg["From"] = "your@gmail.com"
msg["To"] = "target@gmail.com"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("your@gmail.com", "your_app_password")
server.send_message(msg)
server.quit()

print("Email sent.")
