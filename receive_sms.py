from flask import Flask, request, Response, redirect
from twilio.twiml.messaging_response import MessagingResponse
import phonenumbers
from phonenumbers import geocoder
from opencage.geocoder import OpenCageGeocode
import keys

app = Flask(__name__)
usernum=''

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():

    #Now get the user's message input
    usernum = request.values.get('Body')

    response = MessagingResponse()
#send prompt message to user anytime they message
    if usernum.startswith("+") is False:
            response.message("Welcome to Should_I_Reply. Enter a phone number to decide if you want to contact them back"+"\n\nEnter area code, then phone number (Ex: +1781XXXXXXX): ")

    elif usernum.startswith("+"):
            # get phonenum from user through the prompt

            # STEP 1: PARSING PHONE NUMBER FOR USER LOCATION
            number = phonenumbers.parse(usernum)
            # get location of phone num
            location = geocoder.description_for_number(number, "en")
            print(location)

            key = keys.key  # unique api key

            geocode = OpenCageGeocode(key)  # pass out api key inside the function
            query = str(location)
            if query == "":
                response.message("Invalid phone number, try again")
            else:
                response.message("This phone number originates from: " + query + ". Proceed with caution!")


#Response returned depends on whether input phonenum is received from user
    return Response(str(response), mimetype="application/xml")


if __name__ == "__main__":
    app.run(debug=True)