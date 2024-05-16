# import package
import africastalking
# Initialize SDK


def send_sms(phone,name,station):
    username = "sandbox" 
    api_key = "63844ecae6efdf704ed70d2240b823184d6c48419258a10fcda65ab2847718ab"
    africastalking.initialize(username, api_key)
    sms = africastalking.SMS
    response = sms.send(f"Hello {name}, your ID has been foud please come pick it up at {station} as soon as possible..", [phone], 'TUMEIGET')
    # print(response)

