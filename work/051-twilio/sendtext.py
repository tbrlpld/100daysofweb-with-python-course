# -*- coding: utf-8 -*-

"""Mini script to send a text to my self."""

import os
import uuid

from twilio.rest import Client


my_phone_number = os.environ["MY_PHONE_NUMBER"]
twilio_phone_number = os.environ["TWILIO_PHONE_NUMBER"]
twilio_account_sid = os.environ["TWILIO_ACCOUNT_SID"]
twilio_auth_token = os.environ["TWILIO_AUTH_TOKEN"]


client = Client(twilio_account_sid, twilio_auth_token)

uuid_code = uuid.uuid4().hex

client.messages.create(
    to=my_phone_number,
    from_=twilio_phone_number,
    body="Here is your code you wanted: {0}".format(uuid_code),
)
