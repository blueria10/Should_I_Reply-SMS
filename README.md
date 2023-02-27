# Should_I_Reply-SMS
SMS based flask-app 

Have you ever received a call or text from an unknown number, and you're not sure whether or not it's spam, family calling from your native land, or even an acquaintance's number you forgot to save? I definitely have.
Should_I_Reply uses programming for SMS. With Twilio APIs and the Flask framework, a messaging "bot" was created. All users have to do is text this phone number:
![download](https://user-images.githubusercontent.com/85198940/221458132-778595ab-e56a-44fc-8823-73ea1915aab8.png)


Once the phone number receives a message (anything excluding messages starting with "+..."), the bot will automatically send a response talking about what the service is for. Next, the user is prompted to enter a phone number starting with "+(areacode)". Once the user inputs the phone number, if input correctly, the user will receive another message telling them the origin of the phone number. 

It is then up to the user to decide whether or not they want to contact the number. 

Here is a demo video that shows how the messaging service works:


https://user-images.githubusercontent.com/85198940/221461433-79fdc76c-dd73-4350-88b5-f9eb6f97cf56.mp4

