# Copyright 2018 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from __future__ import print_function

import datetime

from firebase_admin import messaging


def send_multicast(log_filename:str, registration_tokens:list=[], **kwargs:dict):
    # These registration tokens come from the client FCM SDKs.
    if (kwargs.get('url')):
        message = messaging.MulticastMessage(
            data = {
                "type": kwargs.get('code'),
                "url": kwargs.get('url'),
                "title": kwargs.get('title'),
                "body": kwargs.get('body'),
                "description": kwargs.get('body'),
                'source': 'jefatura',
                'imageUrl': kwargs.get('image')
            },
            tokens=registration_tokens,
        )
    else:
        message = messaging.MulticastMessage(
            notification=messaging.Notification(
                title= kwargs.get('title'),
                body= kwargs.get('body'),
            ),
            data = {
            },
            tokens=registration_tokens,
        )

    response = messaging.send_each_for_multicast(message)
    responses = response.responses
    failed_tokens = []

    for idx, resp in enumerate(responses):
        with open(log_filename, 'a') as f:
            datetime_lote = datetime.datetime.now(
                datetime.timezone(datetime.timedelta(0))
            ).astimezone()

            status = 1 if resp.success else 0
            f.write( f'{status},{registration_tokens[idx]},{datetime_lote}\n' )

        if not resp.success:
            # The order of responses corresponds to the order of 
            # the registration tokens.
            failed_tokens.append(registration_tokens[idx])
            print(f'List of tokens that caused failures: {failed_tokens}')
            
    return responses