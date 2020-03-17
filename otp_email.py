import smtplib
user_email = "rndjsports@gmail.com"
user_password = "rndjsports123"
send_to_address = "sanketyou8@gmail.com"
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
print("server started")
#Next, log in to the server
server.login(user_email,user_password)
print("success")
#Send the mail
msg = '''Hey, Siddhi! I'm Sundar from Google.
I'm pleased to inform you that you have been selected for working with us.
We were impress by your work on BlockChain Technology and wish to hire you as an intern at the New York Campus of Google.Inc
Please feel free to mail me at my email address for any other queries.
Hoping to work with you 

Sundar Pichai
CEO
Google.Inc
'''
msg1 = '''Thank you for registering with us. Our relationship is based on trust. It's our job to protect your business 
from conterfeiting agencies. You are just one step away from securing your business. Please click on the verification link below to verify your account.
link here ----
    
Please dont share this link with anyone.
    

Chaining security with ---name ---
'''
 # The /n separates the message from the headers
server.sendmail("rndjsports@gmail.com",send_to_address,msg1)
print("sent")
server.close()