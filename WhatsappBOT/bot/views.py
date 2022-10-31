from django.http import HttpResponse
from django.shortcuts import render
from twilio.rest import Client
from django.views.decorators.csrf import csrf_exempt
import requests
from twilio.twiml.messaging_response import MessagingResponse
from PIL import Image
import pytesseract
import io


from googleapiclient.discovery import build
api_key="AIzaSyDsodmmoqOzxcaOpfHB2yaV2SVwgpmdzLA"   #google custom search api key



# twilio whastapp api 
account_sid='AC0dce681fa3ce2afe4868e7a97000f53a'
auth_token='77a94298c8d0a173002f2d81c8039702'
client=Client(account_sid,auth_token)

# Create your views here.

@csrf_exempt
def bot(request):
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    Fetch_msg= request.POST
    print("Fetch_msg-->",Fetch_msg)
    txt=''
    try: # Storing the file that user send to the Twilio whatsapp number in our computer
        msg_url=request.POST.get('MediaUrl0')  # Getting the URL of the file
        print("msg_url-->",msg_url)
        msg_ext=request.POST.get('MediaContentType0')  # Getting the extension for the file
        print("msg_ext-->",msg_ext)
        ext = msg_ext.split('/')[-1]
        print("ext-->",ext)
        
        path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        response = requests.get(msg_url)
        # print( type(response) ) # <class 'requests.models.Response'>
        img = Image.open(io.BytesIO(response.content))
        # print( type(img) ) # <class 'PIL.JpegImagePlugin.JpegImageFile'>



        # Providing the tesseract
        # executable location to pytesseract library

        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

        # Passing the image object to
        # image_to_string() function
        # This function will
        # extract the text from the image
        txt = pytesseract.image_to_string(img)

        # Displaying the extracted text
        print(txt[:-1])
        



        if msg_url != None:
            json_path = requests.get(msg_url)
            filename = msg_url.split('/')[-1]
            open(filename+"."+ext, 'wb').write(json_path.content)  # Storing the file
    except:
        print("no url-->>")

    msg = request.POST.get.lower()  # Reading the message from the whatsapp
    print("msg-->",msg)
    resp = MessagingResponse()
    reply=resp.message()

    # Text response
    if msg == "hi":
       reply.body("Hello Student! Thank you for registering with us\nIn what form is your question? \n\n1.Photo \n2.Text ")

    # Image response
    elif msg == "2":
       reply.body("Type Your Question🤔")
    # feedback response
    elif msg == "yes":
       reply.body("thanks for using our services")
    # feedback response
    elif msg == "no":
       reply.body("send your question to klatch or send to to mentor")
       reply.body("react accpdingly")
    
    # Audio response
    elif msg == "audio":
       reply.media('http://www.largesound.com/ashborytour/sound/brobob.mp3')
        
    # Video response
    elif msg == "video":
       reply.media('https://www.appsloveworld.com/wp-content/uploads/2018/10/640.mp4')
    
    # Document response
    elif msg == "file":
       reply.media('http://www.africau.edu/images/default/sample.pdf')
    
    else:
      if(txt!=''):
         msg=txt
      reply.body("Here are the answers to your Question")
      # google cloud cse custom search api 
      resource = build("customsearch", 'v1', developerKey=api_key).cse()
      result = resource.list(q=msg, cx='e1227369aaad643a0').execute()
      for item in result['items']:
         print(item['link'])
         reply.body("\n")
         reply.body(item['link'])
    reply.body("Are you satisfied \nReact Accodingly (yes or no)")

    return HttpResponse(resp)


