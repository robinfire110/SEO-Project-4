from twilio.rest import Client

account_sid = "AC8024bc8fe84f1d7c1a2adf1fb26b9d82"
auth_token  = "2abb68d3408ad0ed7230f11d9a102180"

def sendMessage(phone_number, food_list):
    """Sends an SMS message containing food about to expire"""
    client = Client(account_sid, auth_token)

    if len(food_list) > 0:
        messageStr = ""
        
        for food_item in food_list:
            messageStr += f"The item {food_item[0]} is about to expire in {food_item[1]} days ({food_item[2]})\n"
        message = client.messages.create(to = f"{phone_number}", from_ = "+19707164530", body = f"{messageStr}")
        print(message.sid)
