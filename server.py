
from __future__ import print_function
from flask import Flask, render_template, redirect, request, url_for
from twilio.rest import TwilioRestClient
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
# from resizeimage import resizeimage
import jinja2
import os
from pathlib import Path
# import pyimgur
import shutil
from helper import get_size, make_jpg, make_url, image_sizing, process_display_message_list, background_process


# imgur clientid=ffa486c0af07526
# imgur clientsecret=17d873e720306db38e3dc7184def600187d40d88

app = Flask(__name__)
app.secret_key = "ABC"
app_key = 'c56aqb698ik1tik'
app_secret = 'zm4auh5hzrcybq5'
app.jinja_env.lstrip_blocks = False


@app.route('/')
def homepage():
    """Register page."""
    my_file = Path("testing.jpg")
    if my_file.is_file():
        os.remove("testing.jpg")
    return render_template("homepage.html")


@app.route('/homepage', methods=['GET'])
def get_form():
    return render_template("homepage.html")


@app.route('/process_card', methods=['POST'])
def process():
    sender_name = request.form.get("sender_name")
    sender_phone = request.form.get("sender_phone")
    recipient_name = request.form.get("recipient_name")
    recipient_phone = request.form.get("recipient_phone")
    copy = request.form.get("copy")
    message = request.form.get("message")
    display_message_list = message.splitlines()
    display_message_list = display_message_list[:5]
    message = "\n".join(display_message_list)
    size = get_size(display_message_list)
    display_message_list = process_display_message_list(display_message_list)

    background = request.form.get("card")
    background, style, im, color = background_process(background,size)
    print("IM: ",im)
    with open("message.txt",'w') as message_send:
        message_send.write(message)
    image = make_jpg(im,color,size)
    url_to_image = make_url('testing.jpg')
    print("URL TO IMAGE: ",url_to_image)
    return render_template('cardpreview.html', 
                           background=background,
                           sender_name=sender_name,
                           sender_phone=sender_phone,
                           recipient_name=recipient_name,
                           recipient_phone=recipient_phone,
                           message=message,
                           display_message_list=display_message_list,
                           style=style,
                           size=size,
                           copy=copy,
                           url_to_image=url_to_image,
                           )

@app.route('/send_card',methods=['POST'])
def sending():
    print("In sending")
    sender_name = request.form.get("sender_name")
    sender_phone = request.form.get("sender_phone")
    recipient_name = request.form.get("recipient_name")
    recipient_phone = request.form.get("recipient_phone")
    copy = request.form.get("copy")
    action = request.form.get("action")  
    message = request.form.get("message")
    background = request.form.get("background")
    size = request.form.get("size")
    sender_phone = str(sender_phone)
    recipient_phone = "+1" + str(recipient_phone)
    url_to_image = request.form.get("url_to_image")
    sending_twilio(recipient_name,recipient_phone,sender_name,sender_phone,message,url_to_image,copy)
    return render_template('homepage.html')

 

def sending_twilio(recipient_name,recipient_phone,sender_name,sender_phone,message,url_to_image,copy):
    """sending the image via twilio """
    sender_phone = sender_phone[:3] + "-" + sender_phone[3:6] + "-" + sender_phone[6:]
    message = recipient_name + ", This is " + sender_name + ".   Please do not reply to this twilio message. Use "+ sender_phone + " to reply."
    media_url = url_to_image
    account_sid = os.environ['account_sid']
    auth_token = os.environ['auth_token']
    client = TwilioRestClient(account_sid, auth_token)
    message = client.messages.create(to=recipient_phone, from_="+16502810894",
                                         body=message, media_url=media_url)
    if copy == "y":
        message = sender_name + ", This is a copy of the mms you sent to " + recipient_name + "."
        message = client.messages.create(to=sender_phone, from_="+16502810894",
                                         body=message, media_url=media_url)
        
      
                               


if __name__ == '__main__':
    PORT = int(os.environ.get("PORT",5000))    
    app.run(host="0.0.0.0", port=PORT)
    

