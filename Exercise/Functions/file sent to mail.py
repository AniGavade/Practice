import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("aniruddhag87@gmail.com", "keuahbnuyxmjgqpa")
server.sendmail('aniruddhag87@gmail.com', 'sanjaytathe98@gmail.com', 'Hi Sanjay, this Mail sent from python terminal.')
print("Mail sent successfully.")
