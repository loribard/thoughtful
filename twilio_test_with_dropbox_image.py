from twilio.rest import TwilioRestClient

def sending():
    """sending the image via twilio """
    URL = 'http://www.expnet.com/expweb.nsf/p/DVD-800/$file/DVD800.jpg'
    # URL = 'https://www.dropbox.com/s/nqwhzrqnf1rtd30/tobesent.jpg'
    media_url = URL
    media_url = "https://www.dropbox.com/s/nqwhzrqnf1rtd30/tobesent.jpg?raw=1" 
    recipient_name = "Lori"
    recipient_phone = "+16508672067"
    sender_name = "LorifromTwilio"
    message = "I wish this would work!"
    account_sid = "AC799808b088f5f4587cab4eaab6d5d857"
    auth_token = "1827f6255d11dd39d7d98712428fab8f"
    client = TwilioRestClient(account_sid, auth_token)
    message = client.messages.create(to=recipient_phone, from_="+16502810894",
                                         body=message,media_url=media_url)



sending()