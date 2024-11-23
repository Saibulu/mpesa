import json
import base64
from datetime import datetime
import requests
from  requests.auth import HTTPBasicAuth
import os


class credentials:
    consumer_key ="7zeAP9wdO96f7keGsTCIumfhXGTh0a3JOWnlPHobubCM0qkO"
    consumer_secret ="AQP0rgR2kYeviX8nuoxEAtikyAFz3lAvfvVpe1N4N7yLsomZd6kDb7EGRnrL2ypt"
    passkey ="bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"
    api_url ="https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"

class MpesaAcessToken:
    token =requests.get(credentials.api_url, auth=HTTPBasicAuth(credentials.consumer_key, credentials.consumer_secret))
    access_token = json.loads['token.text']
    validated_token = access_token['access_token']


class MpesaPassword:
    timestamp =datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    shortcode ="174379"
    passkey =credentials.passkey


    encode_str =shortcode + passkey +timestamp

    encoded = base64.b64encode(encode_str.encode())

    decoded_password =encoded.decode('utf-8')

