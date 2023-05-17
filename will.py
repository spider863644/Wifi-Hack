from infobip_api_client.api_client import ApiClient, Configuration
from infobip_api_client.model.sms_advanced_textual_request import SmsAdvancedTextualRequest
from infobip_api_client.model.sms_destination import SmsDestination
from infobip_api_client.model.sms_response import SmsResponse
from infobip_api_client.model.sms_textual_message import SmsTextualMessage
from infobip_api_client.api.send_sms_api import SendSmsApi
from infobip_api_client.exceptions import ApiException

print ('# ' + '=' * 78)
print ('Author: ' + "__AnonWill__")
print ('Teammates: ' "__SpiderAnonGreyHat" + ", " + "DreamTeam__") 
print ('Copyright: ' + "__copyright 2023","WillSpidey__")
print ('Credits: ' + "__SpiderAnonGreyHat__") 
print ('License: ' + " __WILLSPI__")
print ('Version: ' + "__1.0.1__")
print ('Maintainer: ' + "__SpiderAnon","AnonWill__")
print ('Email: ' + "__testanonwill@gmail.com__")
print ('Status ' + "__prototype__")
from datetime import date
date = date.today()
print("Date:", date)
print ('Username: ' + "__Admin__")
print ('Description: ' + " __First Py CID sms gateway__")
print ('# ' + '=' * 78)



"""
 * Send an sms message by using API.
 *
 * This example is already pre-populated with your account data:
 * 1. Your account Base URL
 * 2. Your account API key
 * 3. Your recipient phone number
 *
 * THIS CODE EXAMPLE IS READY BY DEFAULT. HIT RUN TO SEND THE MESSAGE!

"""

BASE_URL = "https://4mln4m.api.infobip.com"
API_KEY = "e720fb8277a9d97986a6710f004b21b2-bcf73a22-1f67-470d-9f3f-2532f416310c"

SENDER = input("Enter sender ID: ")
RECIPIENT = "13302995218"
MESSAGE_TEXT = input("Enter text message: ")

client_config = Configuration(
        host= BASE_URL,
        api_key={"APIKeyHeader": API_KEY},
        api_key_prefix={"APIKeyHeader": "App"},
    )

api_client = ApiClient(client_config)

sms_request = SmsAdvancedTextualRequest(
        messages=[
            SmsTextualMessage(
                destinations=[
                    SmsDestination(
                        to=RECIPIENT,
                    ),
                ],
                _from=SENDER,
                text=MESSAGE_TEXT,
            )
        ])

api_instance = SendSmsApi(api_client)

try:
    api_response: SmsResponse = api_instance.send_sms_message(sms_advanced_textual_request=sms_request)
    print(api_response)
except ApiException as ex:
    print("Error occurred while trying to send SMS message.")
    print(ex)