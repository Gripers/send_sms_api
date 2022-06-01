import random
import requests
from django.conf import settings


def send_otp_to_phone(phone_number):
    try:
        otp = random.randint(100000, 999999)
        url = 'https://api.smsfly.uz/'
        credentials = {
            "key": "d6400af4-fa5f-11eb-9bd9-0242ac120002",
            "phone": str(phone_number),
            "message": str(otp)
        }
        response = requests.post(url, json=credentials)
        return otp
    except Exception as e:
        print(e)
    return None
