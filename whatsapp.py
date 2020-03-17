from twilio.rest import Client

def send_whatsapp(phone,text):
    account_sid = 'AC68e98a1817c740a043326ec6e46c8283'
    auth_token = 'a1a6665f9321c075685ed0375aac8031'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                              body= text                     ,

                              from_='whatsapp:+14155238886',
                              to='whatsapp:+91'+phone
                          )

    print(message.sid)

text = '''
Updates for TAP clubs this Saturday.

Electronics and Coding 
Amogh      7021004079        Absent

Public Speaking                  
Sanket      9167082806        Present 

ANY CRITICAL UPDATES GOES HERE 
'''
phones=['7021004079','9167082806','9702949555','9137739416']
for phone in phones:
    send_whatsapp(phone,text)