import smtplib

# email = "anand13122003@gmail.com"
# password = "yxpgcdsatxpofmny"
email = "raviravula12@gmail.com"
password = "zrizzrcttkxpor"

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=email, password= password)
    connection.sendmail(from_addr=email,to_addrs="aananddshukla@gmail.com",msg="Subject: Happy Birthday\n\n This is the body of the mail")
