# import package
import africastalking
# Initialize SDK


def send_sms(phone):
    username = "sandbox" 
    api_key = "63844ecae6efdf704ed70d2240b823184d6c48419258a10fcda65ab2847718ab"
    africastalking.initialize(username, api_key)
    sms = africastalking.SMS
    response = sms.send("Your ID has been fooud please come pick it up as soon as possible..", [phone], '2meiget')
    print(response)

